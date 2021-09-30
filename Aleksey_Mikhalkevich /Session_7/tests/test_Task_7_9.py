import unittest

from Session_7.Task_7_9 import EvenRange


class TestTask(unittest.TestCase):

    def setUp(self) -> None:
        self.it1 = EvenRange(7, 11)
        self.it2 = EvenRange(3, 14)

    def test_case_invalid_init(self):
        self.assertRaises(TypeError, EvenRange, "1", 1)
        self.assertRaises(TypeError, EvenRange, "", "3")

    def test_case_next(self):
        self.assertEqual(self.it1.__next__(), 8)
        self.assertEqual(self.it1.__next__(), 10)
        self.assertEqual(self.it1.__next__(), "Out of numbers!")
        self.assertEqual(self.it1.__next__(), "Out of numbers!")


if __name__ == '__main__':
    unittest.main()
