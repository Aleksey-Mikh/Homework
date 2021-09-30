import unittest

from Session_7.Task_7_11 import endless_fib_generator


class TestTask(unittest.TestCase):

    def setUp(self) -> None:
        self.gen = endless_fib_generator()

    def test_case_gen(self):
        self.assertEqual(next(self.gen), 1)
        self.assertEqual(next(self.gen), 1)
        self.assertEqual(next(self.gen), 2)
        self.assertEqual(next(self.gen), 3)
        self.assertEqual(next(self.gen), 5)
        self.assertEqual(next(self.gen), 8)
        self.assertEqual(next(self.gen), 13)


if __name__ == '__main__':
    unittest.main()
