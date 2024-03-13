from unittest import TestCase, main


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTest(TestCase):

    def setUp(self):
        self.integer_list = IntegerList("Poppy", "1", 50, 2.5, 30)

    def test_correct_innit_and_get_data(self):
        self.assertEqual([50, 30], self.integer_list.get_data())

    def test_add_operations_adds_integer_to_list(self):
        expected_result = self.integer_list.get_data() + [5]
        curr_data = self.integer_list.add(5)
        self.assertEqual(expected_result, curr_data)

    def test_add_operations_float_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(5.5)
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_remove_index_operation_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(100)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_remove_element_from_index_in_range(self):
        expected_result = [50]
        del_el = 30
        curr_del_el = self.integer_list.remove_index(1)
        self.assertEqual(self.integer_list.get_data(), expected_result)
        self.assertEqual(del_el, curr_del_el)

    def test_get_element_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(100)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_get_element_valid_index(self):
        expected_result = 50
        element = self.integer_list.get(0)
        self.assertEqual(expected_result, element)

    def test_insert_element(self):
        expected_result = [50, 10, 30]
        self.integer_list.insert(1, 10)
        self.assertEqual(self.integer_list.get_data(), expected_result)

    def test_insert_element_on_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(20, 10)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_insert_float_element_not_integer_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 5.5)
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_get_biggest_expect_success(self):
        self.assertEqual(50, self.integer_list.get_biggest())

    def test_get_index_expect_success(self):
        self.assertEqual(0, self.integer_list.get_index(50))


if __name__ == "__main__":
    main()