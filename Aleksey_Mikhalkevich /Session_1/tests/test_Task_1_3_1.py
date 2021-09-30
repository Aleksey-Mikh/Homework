import unittest

from Session_1 import Task_1_3_1


class TestTask(unittest.TestCase):
    def test_1_get_sorted_unique_sequence(self):
        string = "red,white,black,red,green,black"
        result = ["black", "green", "red", "white"]
        self.assertEqual(Task_1_3_1.get_sorted_unique_sequence(string), result)

    def test_2_get_sorted_unique_sequence(self):
        string = "Humans,are,generally,good,at,noticing,beautiful,things,."
        result = [
            ".", "Humans", "are", "at", "beautiful", "generally", "good", "noticing", "things",
        ]
        self.assertEqual(Task_1_3_1.get_sorted_unique_sequence(string), result)


if __name__ == '__main__':
    unittest.main()
