import unittest

from Session_1 import Task_1_6_2


class TestTask(unittest.TestCase):
    def test_1_get_data_for_table(self):
        data = ['a = 1', 'b = 2', 'c = 3', 'd = 7']
        result = [1, 3], [3, 8]
        self.assertEqual(Task_1_6_2.get_data_for_table(data), result)

    def test_2_get_data_for_table(self):
        data = ['a = 3', 'b = 5', 'c = 2', 'd = 8']
        result = [3, 6], [2, 9]
        self.assertEqual(Task_1_6_2.get_data_for_table(data), result)

    def test_1_check_data(self):
        data = [1, 3], [3, 8]
        result = True
        self.assertEqual(Task_1_6_2.check_data(*data), result)

    def test_2_check_data(self):
        data = [7, 6], [2, 9]
        result = False
        self.assertEqual(Task_1_6_2.check_data(*data), result)

    def test_3_check_data(self):
        data = [7, 6], [10, 9]
        result = False
        self.assertEqual(Task_1_6_2.check_data(*data), result)


if __name__ == '__main__':
    unittest.main()
