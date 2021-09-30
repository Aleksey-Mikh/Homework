import unittest
import filecmp
import time

from Session_7.Task_7_3.Task_7_3 import track_entry_and_exit


class TestTask(unittest.TestCase):

    def test_case(self):
        self.case_check_decorator()
        self.assertTrue(filecmp.cmp("files/example.log", "files/example_correct.log"))

    @staticmethod
    def case_check_decorator():

        @track_entry_and_exit("func - activity")
        def activity():
            time.sleep(5)

        activity()


if __name__ == '__main__':
    unittest.main()
