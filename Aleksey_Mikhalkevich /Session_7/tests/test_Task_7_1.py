import unittest
import filecmp

from Session_7.Task_7_1.Task_7_1 import FileOpen, FilePathNotFoundError


class TestTask(unittest.TestCase):

    def test_case_1(self):
        self.assertRaises(FilePathNotFoundError, self.case_invalid_file_name)

    def test_case_2(self):
        self.case_valid_file_name()
        self.assertTrue(filecmp.cmp("files/unsorted_names_check.txt", "files/unsorted_names_correct.txt"))

    @staticmethod
    def case_invalid_file_name():
        with FileOpen('invalid_file_name.txt') as file:
            data = file.readlines()

    @staticmethod
    def case_valid_file_name():
        with FileOpen("files/unsorted_names.txt") as file_r, \
                FileOpen("files/unsorted_names_check.txt", "w") as file_w:
            data = file_r.readlines()
            data.reverse()
            file_w.writelines(data)


if __name__ == '__main__':
    unittest.main()
