import unittest

from Session_1 import Task_1_5


class TestTask(unittest.TestCase):
    def test_1_get_unique_values(self):
        data = [
            {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
            {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
        ]
        result = {'S005', 'S002', 'S007', 'S001', 'S009'}
        self.assertEqual(Task_1_5.get_unique_values(data), result)

    def test_2_get_unique_values(self):
        data = [{"b": 10, "a": 5, "c": 7, "d": 1}]
        result = {1, 5, 7, 10}
        self.assertEqual(Task_1_5.get_unique_values(data), result)


if __name__ == '__main__':
    unittest.main()
