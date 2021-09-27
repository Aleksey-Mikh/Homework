import unittest

from Session_6 import Task_6_7


class TestTask(unittest.TestCase):

    def setUp(self):
        self.dollars = Task_6_7.Money(15)
        self.bel_r = Task_6_7.Money(10, "BYN")
        self.eur = Task_6_7.Money(20, "EUR")

    def test_case_addition_subtraction(self):
        self.assertEqual(self.dollars + self.bel_r, Task_6_7.Money(19.76))
        self.assertEqual(self.dollars + 10, Task_6_7.Money(25))
        self.assertEqual(10 + self.dollars, Task_6_7.Money(25))
        self.assertEqual(20 - self.dollars, Task_6_7.Money(5))
        self.assertEqual(self.eur - 10, Task_6_7.Money(10.7, "EUR"))
        self.assertEqual(self.eur + 10, Task_6_7.Money(29.3, "EUR"))
        self.assertEqual(40 - self.eur, Task_6_7.Money(18.49))

    def test_sum(self):
        self.assertEqual(sum([self.bel_r, self.dollars, self.eur]), Task_6_7.Money(86.66, "BYN"))

    def test_comparison(self):
        self.assertTrue(self.dollars > self.bel_r)
        self.assertFalse(self.dollars < self.bel_r)
        self.assertTrue(self.dollars >= self.bel_r)
        self.assertFalse(self.dollars <= self.bel_r)
        self.assertTrue(self.dollars == self.dollars)
        self.assertTrue(self.dollars != self.bel_r)

    def test_division_multiplication(self):
        self.assertRaises(ZeroDivisionError, self.dollars.__truediv__, 0)
        self.assertEqual(self.eur / 10, Task_6_7.Money(2))
        self.assertEqual(10 / self.eur, Task_6_7.Money(0.5))
        self.assertEqual(self.eur * 10, Task_6_7.Money(200))
        self.assertEqual(5 * self.eur, Task_6_7.Money(100))


if __name__ == '__main__':
    unittest.main()
