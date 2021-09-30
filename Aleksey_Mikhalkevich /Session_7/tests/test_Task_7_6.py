import unittest

from Session_7.Task_7_6 import get_set_prime_numbers, check_goldbachs_conjecture


class TestTask(unittest.TestCase):

    def setUp(self) -> None:
        self.pr1 = get_set_prime_numbers(16)
        self.pr2 = get_set_prime_numbers(26)

    def test_case_invalid_init(self):
        self.assertCountEqual(self.pr1, {2, 3, 5, 7, 11, 13})
        self.assertCountEqual(self.pr2, {2, 3, 5, 7, 11, 13, 17, 19, 23})

    def test_case_goldbachs_conjecture(self):
        self.assertEqual(check_goldbachs_conjecture(16, self.pr1), "16 = 3 + 13")
        self.assertEqual(check_goldbachs_conjecture(26, self.pr2), "26 = 3 + 23")


if __name__ == '__main__':
    unittest.main()
