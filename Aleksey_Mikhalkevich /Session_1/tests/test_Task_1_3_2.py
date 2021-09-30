import unittest

from Session_1 import Task_1_3_2


class TestTask(unittest.TestCase):
    def test_1_get_divisors_of_number(self):
        number = 60
        result = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
        self.assertEqual(Task_1_3_2.get_divisors_of_number(number), result)

    def test_2_get_divisors_of_number(self):
        number = 40
        result = [1,  2,  4,  5,  8,  10,  20,  40]
        self.assertEqual(Task_1_3_2.get_divisors_of_number(number), result)


if __name__ == '__main__':
    unittest.main()
