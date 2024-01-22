class ClimbingRobot:
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def __init__(self, category: str, part_type: str, capacity: int, memory: int):
        self.category = category
        self.part_type = part_type
        self.capacity = capacity
        self.memory = memory
        self.installed_software = []

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Category should be one of {self.ALLOWED_CATEGORIES}")
        self.__category = value

    def get_used_capacity(self):
        return sum(s['capacity_consumption'] for s in self.installed_software)

    def get_available_capacity(self):
        return self.capacity - self.get_used_capacity()

    def get_used_memory(self):
        return sum(s['memory_consumption'] for s in self.installed_software)

    def get_available_memory(self):
        return self.memory - self.get_used_memory()

    def install_software(self, software: {str, int}):
        if self.get_available_capacity() >= software['capacity_consumption'] and \
                self.get_available_memory() >= software['memory_consumption']:
            self.installed_software.append(software)
            return f"Software '{software['name']}' successfully installed on {self.category} part."
        else:
            return f"Software '{software['name']}' cannot be installed on {self.category} part."

import unittest


class TestClimbingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Legs", 100, 100)

    def test_init(self):
        self.assertEqual(self.robot.category, "Mountain")
        self.assertEqual(self.robot.part_type, "Legs")
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 100)
        self.assertEqual(self.robot.installed_software, [])

    def test_category_setter_with_invalid_value_should_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Invalid"
        self.assertEqual(str(ex.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_install_software_with_enough_capacity_and_memory_should_install_it_and_return_message(self):
        message = self.robot.install_software({"name": "Test", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(message, "Software 'Test' successfully installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [{"name": "Test", "capacity_consumption": 10, "memory_consumption": 10}])


    def test_install_software_with_not_enough_capacity_should_not_install_it_and_return_message(self):
        # First install a software that consumes some capacity but leaves enough memory
        self.robot.install_software({"name": "Partial", "capacity_consumption": 95, "memory_consumption": 10})

        # Attempt to install a software that requires more capacity than available
        message = self.robot.install_software({"name": "TooBig", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(message, "Software 'TooBig' cannot be installed on Mountain part.")

        # Ensure the 'TooBig' software was not installed
        self.assertNotIn({"name": "TooBig", "capacity_consumption": 10, "memory_consumption": 10},
                         self.robot.installed_software)

        # Ensure that the capacity is correctly calculated after the failed installation attempt
        self.assertEqual(self.robot.get_used_capacity(), 95)
        self.assertEqual(self.robot.get_available_capacity(), 5)

    def test_install_software_with_not_enough_memory_should_not_install_it_and_return_message(self):
        message = self.robot.install_software({"name": "Test", "capacity_consumption": 10, "memory_consumption": 101})
        self.assertEqual(message, "Software 'Test' cannot be installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [])

    def test_get_used_capacity(self):
        self.robot.install_software({"name": "Test", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(self.robot.get_used_capacity(), 10)

    def test_get_available_capacity(self):
        self.robot.install_software({"name": "Test", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(self.robot.get_available_capacity(), 90)

    def test_get_used_memory(self):
        self.robot.install_software({"name": "Test", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(self.robot.get_used_memory(), 10)

    def test_get_available_memory(self):
        self.robot.install_software({"name": "Test", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(self.robot.get_available_memory(), 90)

    def test_invalid_category_initialization_should_raise(self):
        with self.assertRaises(ValueError) as ex:
            ClimbingRobot("Ocean", "Wheels", 50, 50)
        self.assertEqual(str(ex.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_install_software_with_exact_capacity_and_memory_should_install_it(self):
        self.robot.install_software({"name": "ExactFit", "capacity_consumption": 100, "memory_consumption": 100})
        self.assertEqual(len(self.robot.installed_software), 1)
        self.assertEqual(self.robot.get_available_capacity(), 0)
        self.assertEqual(self.robot.get_available_memory(), 0)


if __name__ == "__main__":
    unittest.main()

