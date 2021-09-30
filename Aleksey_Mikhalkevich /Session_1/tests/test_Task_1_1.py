import unittest

from Session_1 import Task_1_1


class TestTask(unittest.TestCase):
    def test_1_calculate_len(self):
        string = "Oh, it is python"
        self.assertEqual(Task_1_1.calculate_len(string), len(string))

    def test_2_calculate_len(self):
        string = "Humans are generally good at noticing beautiful things."
        self.assertEqual(Task_1_1.calculate_len(string), len(string))


if __name__ == '__main__':
    unittest.main()
