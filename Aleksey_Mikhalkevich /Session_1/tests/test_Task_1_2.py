import unittest

from Session_1 import Task_1_2


class TestTask(unittest.TestCase):
    def test_1_char_frequency(self):
        string = "Oh, it is python"
        correct_dict = {
            ",": 1, " ": 3, "o": 2, "h": 2, "i": 2, "t": 2, "s": 1, "p": 1, "y": 1, "n": 1
        }
        self.assertEqual(Task_1_2.get_char_frequency(string), correct_dict)

    def test_2_char_frequency(self):
        string = "aaa bbbb, cc, ddd, e!@!"
        correct_dict = {
            "a": 3, "b": 4, "c": 2, "d": 3, "e": 1, " ": 4, ",": 3, "!": 2, "@": 1
        }
        self.assertEqual(Task_1_2.get_char_frequency(string), correct_dict)


if __name__ == '__main__':
    unittest.main()
