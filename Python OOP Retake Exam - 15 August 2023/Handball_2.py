import unittest


class Trip:
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def __init__(self, budget: float, travelers_number: int, is_family: bool):
        self.budget = budget
        self.travelers = travelers_number
        self.is_family = is_family
        self.booked_destinations_paid_amounts = {}

    @property
    def travelers(self):
        return self._travelers

    @travelers.setter
    def travelers(self, value):
        if value < 1:
            raise ValueError('At least one traveler is required!')
        self._travelers = value

    @property
    def is_family(self):
        return self._is_family

    @is_family.setter
    def is_family(self, value):
        if value and self.travelers < 2:
            self._is_family = False
        else:
            self._is_family = value

    def book_a_trip(self, destination: str):
        if destination not in self.DESTINATION_PRICES_PER_PERSON:
            return 'This destination is not in our offers, please choose a new one!'

        required_price = self.DESTINATION_PRICES_PER_PERSON[destination] * self.travelers
        if self.is_family:
            required_price *= 0.9
        if self.budget < required_price:
            return 'Your budget is not enough!'

        self.booked_destinations_paid_amounts[destination] = required_price
        self.budget -= required_price
        return f'Successfully booked destination {destination}! Your budget left is {self.budget:.2f}'

    def booking_status(self):
        if not self.booked_destinations_paid_amounts:
            return f'No bookings yet. Budget: {self.budget:.2f}'
        result = []
        sorted_bookings = sorted(self.booked_destinations_paid_amounts.items())
        for booked_destination, paid_amount in sorted_bookings:
            result.append(f"""Booked Destination: {booked_destination}
Paid Amount: {paid_amount:.2f}""")
        result.append(f"""Number of Travelers: {self.travelers}
Budget Left: {self.budget:.2f}""")
        return '\n'.join(result)




class TestTrip(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(10000, 2, False)

    def test_init(self):
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(False, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_setter_raises_exception_when_value_is_less_than_1(self):
        with self.assertRaises(ValueError) as context:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(context.exception))

    def test_book_trip_invalid_destination(self):

        self.assertEqual('This destination is not in our offers, please choose a new one!', self.trip.book_a_trip("Invalid"))

    def test_book_trip_not_enough_budget(self):
        self.assertEqual('Your budget is not enough!', self.trip.book_a_trip("New Zealand"))

    def test_book_a_trip_if_destination_is_valid_and_is_family(self):
        self.trip.is_family = True
        self.trip.budget = 3000
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 2100.00', self.trip.book_a_trip("Bulgaria"))
        self.assertEqual(2100, self.trip.budget)
        self.assertEqual({"Bulgaria": 900.0}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_negative_number_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.trip.travelers = -1
        self.assertEqual('At least one traveler is required!', str(context.exception))

    def test_is_family_returns_true_or_false(self):
        trip = Trip(10000, 2, True)
        self.assertEqual(True, trip.is_family)

        trip = Trip(10000, 1, True)
        self.assertEqual(False, trip.is_family)

        trip = Trip(10000, 2, False)
        self.assertEqual(False, trip.is_family)

    def test_booking_status_if_not_booked_destinations_paid_amounts(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.trip.booking_status())

    def test_booking_status_if_true_return_sorted_result(self):
        self.trip.booked_destinations_paid_amounts = {"New Zealand": 7500, "Australia": 5700}
        self.assertEqual("""Booked Destination: Australia"""
                         """\nPaid Amount: 5700.00"""
                         """\nBooked Destination: New Zealand"""
                         """\nPaid Amount: 7500.00"""
                         """\nNumber of Travelers: 2"""
                         """\nBudget Left: 10000.00""", self.trip.booking_status())

if __name__ == '__main__':
    unittest.main()
