"""
Implement a function get_digits(num: int) -> Tuple[int]
which returns a tuple of a given integer's digits.

Examples:
```
Input: 87178291199
Output: (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
"""


def get_digits(num):
    """function returns a tuple of a given integer's digits"""
    return tuple(list(num))


def main():
    num = input("input a number: ")
    tuple_digits = get_digits(num)
    print(tuple_digits)


if __name__ == '__main__':
    main()
