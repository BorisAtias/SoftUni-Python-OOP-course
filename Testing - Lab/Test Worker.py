import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("John", 1000, 5)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 5)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_is_incremented_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 6)

    def test_error_raised_when_working_with_negative_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.worker.work()

        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_error_raised_when_working_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_increases_correctly_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)

    def test_worker_energy_decreases_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 4)

    def test_get_info_returns_correct_string(self):
        info = self.worker.get_info()
        expected_info = "John has saved 0 money."
        self.assertEqual(info, expected_info)

if __name__ == "__main__":
    unittest.main()