import unittest

from Session_7.Task_7_7 import MyNumberCollection


class TestTask(unittest.TestCase):

    def setUp(self) -> None:
        self.col1 = MyNumberCollection(0, 5, 2)
        self.col2 = MyNumberCollection((1, 2, 3, 4, 5))
        self.col3 = MyNumberCollection(0, 5, 3)
        self.col4 = MyNumberCollection(0, 5, 5)
        self.col5 = MyNumberCollection({1, 2, 3, 4, 5})

    def test_case_invalid_init(self):
        self.assertRaises(TypeError, MyNumberCollection, (1, 2, 3, "4", 5))
        self.assertRaises(TypeError, MyNumberCollection, "0", 5, 2)
        self.assertRaises(TypeError, MyNumberCollection, 0, "5", 2)
        self.assertRaises(TypeError, MyNumberCollection, 0, 5, "2")
        self.assertRaises(TypeError, MyNumberCollection, 0,)

    def test_case_invalid_append(self):
        self.assertRaises(TypeError, self.col1.append, "string")
        self.assertRaises(TypeError, self.col2.append, "string")

    def test_case_print(self):
        self.assertEqual(str(self.col1), "[0, 2, 4, 5]")
        self.assertEqual(str(self.col2), "[1, 2, 3, 4, 5]")
        self.assertEqual(str(self.col3), "[0, 3, 5]")
        self.assertEqual(str(self.col4), "[0, 5]")
        self.assertEqual(str(self.col5), "[1, 2, 3, 4, 5]")

    def test_case_add(self):
        self.assertEqual(str(self.col1 + self.col2), "[0, 2, 4, 5, 1, 2, 3, 4, 5]")
        self.assertEqual(str(self.col1), "[0, 2, 4, 5]")
        self.assertEqual(str(self.col2), "[1, 2, 3, 4, 5]")
        self.assertEqual(str(self.col3 + self.col4), "[0, 3, 5, 0, 5]")

    def test_case_gate_item(self):
        self.assertEqual(self.col1[2], 16)
        self.assertEqual(self.col2[4], 25)
        self.assertEqual(self.col3[0], 0)

    def test_case_append(self):
        self.col1.append(3)
        self.assertEqual(str(self.col1), "[0, 2, 4, 5, 3]")
        self.col2.append(3)
        self.assertEqual(str(self.col2), "[1, 2, 3, 4, 5, 3]")
        self.col3.append(3)
        self.assertEqual(str(self.col3), "[0, 3, 5, 3]")
        self.col4.append(3)
        self.assertEqual(str(self.col4), "[0, 5, 3]")


if __name__ == '__main__':
    unittest.main()
