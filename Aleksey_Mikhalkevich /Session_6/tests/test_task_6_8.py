import unittest

from Session_6 import Task_6_8


class TestTask(unittest.TestCase):
    def test_case_1(self):
        self.Pagination = Task_6_8.Pagination('Your beautiful text', 5)

        self.assertEqual(self.Pagination.page_count, 4)
        self.assertEqual(self.Pagination.item_count, 19)

        self.assertEqual(self.Pagination.count_items_on_page(0), 5)
        self.assertEqual(self.Pagination.count_items_on_page(3), 4)
        self.assertRaises(Task_6_8.PaginateError, self.Pagination.count_items_on_page, 4)

        self.assertEqual(self.Pagination.find_page('Your'), [0])
        self.assertEqual(self.Pagination.find_page('e'), [1, 3])
        self.assertEqual(self.Pagination.find_page('beautiful'), [1, 2])
        self.assertRaises(Task_6_8.FindSubStringError, self.Pagination.find_page, 'great')

        self.assertEqual(self.Pagination.display_page(0), "'Your '")

    def test_case_2(self):
        self.Pagination = Task_6_8.Pagination('Your beautiful text', 3)

        self.assertEqual(self.Pagination.page_count, 7)
        self.assertEqual(self.Pagination.item_count, 19)

        self.assertEqual(self.Pagination.count_items_on_page(0), 3)
        self.assertEqual(self.Pagination.count_items_on_page(3), 3)
        self.assertEqual(self.Pagination.count_items_on_page(6), 1)
        self.assertRaises(Task_6_8.PaginateError, self.Pagination.count_items_on_page, 7)

        self.assertEqual(self.Pagination.find_page('Your'), [0, 1])
        self.assertEqual(self.Pagination.find_page('e'), [2, 5])
        self.assertEqual(self.Pagination.find_page('beautiful'), [1, 2, 3, 4])
        self.assertRaises(Task_6_8.FindSubStringError, self.Pagination.find_page, 'great')

        self.assertEqual(self.Pagination.display_page(0), "'You'")


if __name__ == '__main__':
    unittest.main()
