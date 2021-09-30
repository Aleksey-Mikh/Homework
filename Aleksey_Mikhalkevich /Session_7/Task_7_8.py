"""
Implement your custom iterator class called
MySquareIterator which gives squares of
elements of collection it iterates through.
"""


def chek_iter_obj(func):
    """decorator for check iterable object"""

    def wrapper(self, lst):
        try:
            iter(lst)
            return func(self, lst)
        except TypeError:
            raise TypeError(f"{lst} isn't iterable object")

    return wrapper


class MySquareIterator:
    """
    custom iterator class which gives squares of
    elements of collection.
    """

    @chek_iter_obj
    def __init__(self, lst):
        self.lst = lst
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind >= len(self.lst):
            self.ind = 0
            raise StopIteration
        result = self.lst[self.ind]
        self.ind += 1
        return result**2


def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)


if __name__ == '__main__':
    main()
