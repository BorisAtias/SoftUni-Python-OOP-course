import unittest


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class TestCarManager(unittest.TestCase):

    def setUp(self):
        self.car = Car("Skoda", "Octavia", 5, 60)

    def test_innit(self):
        self.assertEqual(self.car.make, "Skoda")
        self.assertEqual(self.car.model, "Octavia")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_no_make_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Octavia", 5, 60)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_no_model_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Skoda", "", 5, 60)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_negative_fuel_consumption_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Skoda", "Octavia", -1, 60)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_negative_fuel_capacity_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Skoda", "Octavia", 5, -60)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_negative_fuel_amount_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount -= 65
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_more_than_capacity_should_fill_to_capacity(self):
        self.car.refuel(80)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_no_exception(self):
        self.car.refuel(60)
        self.car.drive(100)
        fuel_needed = 50
        self.assertEqual(55, self.car.fuel_amount)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")



if __name__ == "__main__":
    unittest.main()