import unittest

from Session_7.Task_7_10 import endless_generator


class TestTask(unittest.TestCase):

    def setUp(self) -> None:
        self.gen = endless_generator()

    def test_case_gen(self):
        self.assertEqual(next(self.gen), 1)
        self.assertEqual(next(self.gen), 3)
        self.assertEqual(next(self.gen), 5)
        self.assertEqual(next(self.gen), 7)
        self.assertEqual(next(self.gen), 9)


if __name__ == '__main__':
    unittest.main()
