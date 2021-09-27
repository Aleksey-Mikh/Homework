from math import ceil


class PaginateError(Exception):
    """
    Class exception which calls when the page
    is not found in list_of_contents.
    """

    def __init__(self, message):
        super().__init__(message)


class FindSubStringError(Exception):
    """
    Class exception which calls when the sub string
    is not found in the text.
    """

    def __init__(self, message):
        super().__init__(message)


class Pagination:
    """
    Pagination class helpful to arrange text on pages
    and list content on given page.
    """

    def __init__(self, text, pagination):
        self.text = text
        self.pagination = pagination
        self.item_count = self._get_item_count()
        self.page_count = self._get_page_count()
        self.list_of_contents = self._get_list_of_contents()

    def _get_page_count(self):
        """Get page count. Protect method, use only inside class."""
        return ceil(len(self.text) / self.pagination)

    def _get_item_count(self):
        """Get item count. Protect method, use only inside class."""
        return len(self.text)

    def _get_list_of_contents(self):
        """
        Get list of a contents. Divides the text into pages
        and defined list_of_delimiter which contains indexes
        of start and end pages in text.
        Protect method, use only inside class.
        """
        list_of_content = []
        self.list_of_delimiter = []
        start_ind, end_ind = 0, self.pagination

        while start_ind < self.pagination * self.page_count:
            list_of_content.append(self.text[start_ind:end_ind])
            self.list_of_delimiter.append((start_ind, end_ind - 1))
            start_ind, end_ind = end_ind, end_ind + self.pagination

        return list_of_content

    def _check_substring_in_text(self, substring):
        """
        Check substring is in the text. If substring isn't
        in the text raise Exception - FindSubStringError.
        Protect method, use only inside class.
        """
        if substring in self.text:
            return True
        else:
            raise FindSubStringError(f"`{substring}` is missing on the pages")

    def _get_index_of_substring_in_text(self, substring):
        len_substring = len(substring)
        count, stop_count = 0, self.text.count(substring)
        list_of_inclusion = []
        ind_for_search = 0

        while count < stop_count:
            ind_inclusion = self.text.find(substring, ind_for_search)
            list_of_inclusion.append(ind_inclusion)
            ind_for_search = ind_inclusion + len_substring
            count += 1

        return list_of_inclusion

    def _find_pages_by_ind(self, list_of_inclusion, substring):
        result_find, long_word = [], False
        for ind in list_of_inclusion:
            for number, tup in enumerate(self.list_of_delimiter):
                if tup[0] <= ind <= tup[1] or long_word:
                    result_find.append(number)
                    end_ind_of_word = ind + len(substring) - 1

                    if tup[0] <= end_ind_of_word <= tup[1]:
                        long_word = False
                        break
                    else:
                        long_word = True

        return result_find

    def find_page(self, substring):
        if self._check_substring_in_text(substring):
            list_of_inclusion = self._get_index_of_substring_in_text(substring)
            return self._find_pages_by_ind(list_of_inclusion, substring)

    def count_items_on_page(self, number_page):
        if len(self.list_of_contents) <= number_page:
            raise PaginateError("Invalid index. Page is missing.")
        return len(self.list_of_contents[number_page])

    def display_page(self, ind):
        return f"{self.list_of_contents[ind]!r}"
