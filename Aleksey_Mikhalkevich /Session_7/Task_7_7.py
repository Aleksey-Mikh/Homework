"""
Implement your custom collection called MyNumberCollection.
It should be able to contain only numbers.
It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there,
exception TypeError should be raised.
Method init sholud be able to take either start,end,step arguments,
where start - first number of collection,
end - last number of collection or some ordered iterable collection
(see the example). Implement following functionality:

1)appending new element to the end of collection.
2)concatenating collections together using +.
3)when element is addressed by index(using []),
user should get square of the addressed element.
4)when iterated using cycle for, elements should be given normally.
5)user should be able to print whole collection as if it was list.
"""


def check_iter_obj(iter_obj):
    """
    check if iter_obj is empty and if one of his element isn't a int.
    """
    if not iter_obj:
        raise TypeError('Iterable object is empty!')

    for number in iter_obj:
        if not isinstance(number, int):
            raise TypeError("MyNumberCollection supports only numbers!")

    return True


def check_value_start(start):
    """
    check value start if it int or iterable object
    else raise TypeError.
    """
    is_iter = False

    if isinstance(start, int):
        return start, is_iter

    elif isinstance(start, (list, set, frozenset, tuple)):
        if check_iter_obj(start):
            is_iter = True
            return start, is_iter

    raise TypeError(f"{start!r} - object is not a number!")


def check_value(value):
    """
    check value if it int else raise TypeError.
    """
    if isinstance(value, int) or value is None:
        return value
    raise TypeError(f"{value!r} - object is not a number!")


def check_data(func):
    """
    Decorator for check data which sent in MyNumberCollection
    """

    def wrapper(self, start, end=None, step=None, *args, **kwargs):
        start, is_iter = check_value_start(start)
        end = check_value(end)
        step = check_value(step)
        kwargs["is_iter"] = is_iter
        return func(self, start, end, step, *args, **kwargs)

    return wrapper


def check_start_end_value(func):
    """
    Decorator for check case when MyNumberCollection
    called only with one arguments.
    """

    def wrapper(self, start, end, step, *args, **kwargs):
        if isinstance(start, int) and end is None:
            raise TypeError("end value is not defined")
        return func(self, start, end, step, *args, **kwargs)

    return wrapper


def check_instance(func):

    def wrapper(self, other):
        if isinstance(other, MyNumberCollection):
            return func(self, other)
        else:
            raise TypeError("Method add can be use only with collections")

    return wrapper


class MyNumberCollection:
    """custom collection it should be able to contain only numbers."""

    @check_data
    @check_start_end_value
    def __init__(self, start, end=None, step=None, *args, **kwargs):
        self.start = start
        self.end = end
        self.step = step
        self.is_iter = kwargs["is_iter"]
        self.collection = self._get_collection()

    def _get_collection(self):
        collection = []
        if self.is_iter:
            collection.extend(self.start)
        else:
            if self.step is None:
                self.step = 1
            collection = [i for i in range(self.start, self.end, self.step)]
            if collection[-1] != self.end:
                collection.append(self.end)

        return collection

    @staticmethod
    def _check_value(number):
        if isinstance(number, int):
            return True
        else:
            raise TypeError(f"{number!r} - object is not a number!")

    def append(self, number):
        if self._check_value(number):
            self.collection.append(number)

    @check_instance
    def __add__(self, other):
        return self.collection + other.collection

    def __len__(self):
        return len(self.collection)

    def __getitem__(self, item):
        return self.collection[item] ** 2

    def __iter__(self):
        return iter(self.collection)

    def __str__(self):
        return f"{self.collection}"

    def __repr__(self):
        return f"{self.collection}"


def main():
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)

    col1.append(7)
    print(col1)

    print(col1 + col2)
    print(col1)
    print(col2)

    print(col2[4])
    for item in col1:
        print(item)


if __name__ == '__main__':
    main()
