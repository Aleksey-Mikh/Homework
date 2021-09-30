import unittest

from Session_1 import Task_1_6_1


class TestTask(unittest.TestCase):
    def test_1_convert_tuple_to_int(self):
        data = (1, 2, 3, 4)
        result = 1234
        self.assertEqual(Task_1_6_1.convert_tuple_to_int(data), result)

    def test_2_convert_tuple_to_int(self):
        data = (1, 3, 4, 6, 9, 0)
        result = 134690
        self.assertEqual(Task_1_6_1.convert_tuple_to_int(data), result)


if __name__ == '__main__':
    unittest.main()
