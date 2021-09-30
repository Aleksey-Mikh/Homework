import unittest

from Session_7.Task_7_8 import MySquareIterator


class TestTask(unittest.TestCase):

    def setUp(self) -> None:
        self.it1 = MySquareIterator([1, 2, 3, 4, 5])
        self.it2 = MySquareIterator((1, 2, 3, 4, 5))
        self.it3 = MySquareIterator({1, 2, 3, 4, 5})

    def test_case_invalid_init(self):
        self.assertRaises(TypeError, MySquareIterator, 1)
        self.assertRaises(TypeError, MySquareIterator, True)

    def test_case_next(self):
        self.assertEqual(self.it1.__next__(), 1)
        self.assertEqual(self.it1.__next__(), 4)
        self.assertEqual(self.it1.__next__(), 9)
        self.assertEqual(self.it2.__next__(), 1)


if __name__ == '__main__':
    unittest.main()
