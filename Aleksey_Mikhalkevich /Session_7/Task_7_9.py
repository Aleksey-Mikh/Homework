"""
Implement an iterator class EvenRange, which accepts start and end
of the interval as an init arguments and gives only even numbers
during iteration. If user tries to iterate after it gave all
possible numbers Out of numbers! should be printed.
Note: Do not use function range() at all
"""


def chek_int_obj(func):
    """decorator for check int object"""

    def wrapper(self, start, end):
        if isinstance(start, int) and isinstance(end, int):
            return func(self, start, end)
        else:
            raise TypeError("start and end value must be integer")

    return wrapper


class EvenRange:
    """
    iterator class which accepts start and end of the interval
    as an init arguments and gives only even numbers during iteration.
    """

    @chek_int_obj
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.number = self.start
        self._iter = False

    def __iter__(self):
        self._iter = True
        return self

    def __next__(self):
        if self.number < self.end - 1:
            while self.number % 2 != 0:
                self.number += 1

            result = self.number
            self.number += 1

            return result

        elif self._iter:
            print("Out of numbers!")
            raise StopIteration
        else:
            return "Out of numbers!"


def main():
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))

    er2 = EvenRange(3, 17)
    for number in er2:
        print(number)


if __name__ == '__main__':
    main()
