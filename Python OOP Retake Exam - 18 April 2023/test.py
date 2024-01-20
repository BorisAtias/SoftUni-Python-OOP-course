class Robot:
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def __init__(self, robot_id: str, category: str, capacity: int, price: float):
        self.robot_id = robot_id
        self.category = category
        self.available_capacity = capacity
        self.price = price
        self.hardware_upgrades = []
        self.software_updates = []

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Category should be one of '{self.ALLOWED_CATEGORIES}'")
        self.__category = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

    def upgrade(self, hardware_component: str, component_price: float):
        if hardware_component in self.hardware_upgrades:
            return f"Robot {self.robot_id} was not upgraded."
        self.hardware_upgrades.append(hardware_component)
        self.price += component_price * self.PRICE_INCREMENT
        return f'Robot {self.robot_id} was upgraded with {hardware_component}.'

    def update(self, version: float, needed_capacity: int):
        if (self.software_updates and version <= max(self.software_updates)) or self.available_capacity < needed_capacity:
            return f"Robot {self.robot_id} was not updated."
        self.software_updates.append(version)
        self.available_capacity -= needed_capacity
        return f'Robot {self.robot_id} was updated to version {version}.'

    def __gt__(self, other):
        if self.price > other.price:
            return f'Robot with ID {self.robot_id} is more expensive than Robot with ID {other.robot_id}.'
        if self.price == other.price:
            return f'Robot with ID {self.robot_id} costs equal to Robot with ID {other.robot_id}.'
        return f'Robot with ID {self.robot_id} is cheaper than Robot with ID {other.robot_id}.'



import unittest


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot("R2D2", "Entertainment", 100, 2000)

    def test_robot_init(self):
        self.assertEqual(self.robot.robot_id, "R2D2")
        self.assertEqual(self.robot.category, "Entertainment")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 2000)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_robot_init_with_invalid_category(self):
        with self.assertRaises(ValueError) as ex:
            Robot("R2D2", "Invalid", 100, 2000)
        self.assertEqual(str(ex.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_robot_init_with_negative_price(self):
        with self.assertRaises(ValueError) as ex:
            Robot("R2D2", "Entertainment", 100, -2000)
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_robot_upgrade_with_already_existing_hardware(self):
        self.robot.hardware_upgrades = ["processor"]
        result = self.robot.upgrade("processor", 100)
        self.assertEqual(result, "Robot R2D2 was not upgraded.")

    def test_robot_upgrade_with_non_existing_hardware(self):
        result = self.robot.upgrade("arm", 100)
        self.assertEqual(result, "Robot R2D2 was upgraded with arm.")
        self.assertEqual(self.robot.hardware_upgrades, ["arm"])
        self.assertEqual(self.robot.price, 2150)

    def test_robot_update_with_already_existing_version(self):
        self.robot.software_updates = [1.0, 1.5]
        result = self.robot.update(1.0, 50)
        self.assertEqual(result, "Robot R2D2 was not updated.")

    def test_robot_update_with_not_enough_capacity(self):
        result = self.robot.update(1.0, 150)
        self.assertEqual(result, "Robot R2D2 was not updated.")

    def test_robot_update_with_valid_data(self):
        result = self.robot.update(1.0, 50)
        self.assertEqual(result, "Robot R2D2 was updated to version 1.0.")
        self.assertEqual(self.robot.software_updates, [1.0])
        self.assertEqual(self.robot.available_capacity, 50)

    def test_robot_gt_with_greater_price(self):
        other_robot = Robot("C3PO", "Entertainment", 100, 1000)
        result = self.robot > other_robot
        self.assertEqual(result, "Robot with ID R2D2 is more expensive than Robot with ID C3PO.")

    def test_robot_gt_with_equal_price(self):
        other_robot = Robot("C3PO", "Entertainment", 100, 2000)
        result = self.robot > other_robot
        self.assertEqual(result, "Robot with ID R2D2 costs equal to Robot with ID C3PO.")

    def test_robot_gt_with_lower_price(self):
        other_robot = Robot("C3PO", "Entertainment", 100, 3000)
        result = self.robot > other_robot
        self.assertEqual(result, "Robot with ID R2D2 is cheaper than Robot with ID C3PO.")


if __name__ == "__main__":
    unittest.main()