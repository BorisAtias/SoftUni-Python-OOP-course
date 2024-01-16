class SecondHandCar:
    def __init__(self, model: str, car_type: str, mileage: int, price: float):
        self.model = model
        self.car_type = car_type
        self.mileage = mileage
        self.price = price
        self.repairs = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 1.0:
            raise ValueError('Price should be greater than 1.0!')
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value <= 100:
            raise ValueError('Please, second-hand cars only! Mileage must be greater than 100!')
        self._mileage = value

    def set_promotional_price(self, new_price: float):
        if new_price >= self.price:
            raise ValueError('You are supposed to decrease the price!')
        self.price = new_price
        return 'The promotional price has been successfully set.'

    def need_repair(self, repair_price: float, repair_description: str):
        if repair_price > self.price / 2:
            return 'Repair is impossible!'
        self.price += repair_price
        self.repairs.append(repair_description)
        return f'Price has been increased due to repair charges.'

    def __gt__(self, other):
        if self.car_type != other.car_type:
            return 'Cars cannot be compared. Type mismatch!'
        return self.price > other.price

    def __str__(self):
        return f"""Model {self.model} | Type {self.car_type} | Milage {self.mileage}km
Current price: {self.price:.2f} | Number of Repairs: {len(self.repairs)}"""


import unittest


class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.car1 = SecondHandCar("Toyota", "Sedan", 15000, 10000.0)
        self.car2 = SecondHandCar("Ford", "SUV", 20000, 15000.0)

    def test_init(self):
        self.assertEqual(self.car1.model, "Toyota")
        self.assertEqual(self.car1.car_type, "Sedan")
        self.assertEqual(self.car1.mileage, 15000)
        self.assertEqual(self.car1.price, 10000.0)
        self.assertEqual(self.car1.repairs, [])
        self.assertEqual(self.car2.model, "Ford")
        self.assertEqual(self.car2.car_type, "SUV")
        self.assertEqual(self.car2.mileage, 20000)
        self.assertEqual(self.car2.price, 15000.0)
        self.assertEqual(self.car2.repairs, [])

    def test_price_greater_than_1(self):
        with self.assertRaises(ValueError) as ex:
            self.car1.price = 0
        self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

    def test_mileage_greater_than_100(self):
        with self.assertRaises(ValueError) as ex:
            self.car1.mileage = 0
        self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_set_promotional_price_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car1.set_promotional_price(10000)
        self.assertEqual(str(ex.exception), "You are supposed to decrease the price!")

    def test_set_promotional_price_success(self):
        self.assertEqual(self.car1.set_promotional_price(5000), "The promotional price has been successfully set.")
        self.assertEqual(self.car1.price, 5000)

    def test_need_repair_return_repair_impossible(self):
        self.assertEqual(self.car1.need_repair(6000, "broken engine"), "Repair is impossible!")

    def test_need_repair_return_price_increase(self):
        self.assertEqual(self.car1.need_repair(5000, "broken engine"), "Price has been increased due to repair charges.")
        self.assertEqual(self.car1.price, 15000)

    def test_compare_cars_returns_missmatch(self):
        self.assertEqual(self.car1 > self.car2, "Cars cannot be compared. Type mismatch!")

    def test_compare_cars_returns_true(self):
        self.assertEqual(self.car2.price > self.car1.price, True)
        self.assertEqual(self.car2.price < self.car1.price, False)

    def test_str_method(self):
        car_str = "Model Toyota | Type Sedan | Milage 15000km\nCurrent price: 10000.00 | Number of Repairs: 0"
        self.assertEqual(str(self.car1), car_str)


if __name__ == '__main__':
    unittest.main()
