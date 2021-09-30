import unittest

from Session_7.Task_7_5 import (
    NumberIsNotEvenError,
    NumberLessThan2Error,
    NumberIsNotNumberError,
    check_number
)


class TestTask(unittest.TestCase):

    def test_case_1(self):
        self.assertRaises(NumberIsNotEvenError, check_number, 3)
        self.assertRaises(NumberLessThan2Error, check_number, 0)
        self.assertRaises(NumberIsNotNumberError, check_number, 'str')
        self.assertRaises(NumberIsNotNumberError, check_number, [])
        self.assertRaises(NumberIsNotNumberError, check_number, set())

    def test_case_2(self):
        self.assertTrue(check_number(4))
        self.assertTrue(check_number(4.0))


if __name__ == '__main__':
    unittest.main()
