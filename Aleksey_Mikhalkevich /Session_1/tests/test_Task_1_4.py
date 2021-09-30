import unittest

from Session_1 import Task_1_4


class TestTask(unittest.TestCase):
    def test_1_get_sorted_dict(self):
        data = {"b": 9, 1: 3, "c": 7, "a": "7", False: 7}
        result = {1: 3, False: 7, "a": "7", "b": 9, "c": 7}
        self.assertEqual(Task_1_4.get_sorted_dict(data), result)

    def test_2_get_sorted_dict(self):
        data = {"b": 10, "a": 5, "c": 7, "d": 1}
        result = {"a": 5, "b": 10, "c": 7, "d": 1}
        self.assertEqual(Task_1_4.get_sorted_dict(data), result)


if __name__ == '__main__':
    unittest.main()
