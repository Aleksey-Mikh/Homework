"""
Implement a function  which, given a list of integers and return
a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array
except the one at `i`.

Examples:
```
Input: [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]
```
"""

from numpy import prod


def foo(list_digits):
    """
    function  which, given a list of integers and return
    a new list such that each element at index `i` of the new list
    is the product of all the numbers in the original array
    except the one at `i`.
    """
    product_numbers = prod(list_digits)  # multiplying numbers in the list
    result_list = []

    for digit in list_digits:
        result_list.append(product_numbers // digit)

    return result_list


def main():
    list_digits = eval(
        input("input a list of integers in format - [1, 2, 3, 4, 5]: ")
    )
    result_list = foo(list_digits)
    print(result_list)


if __name__ == '__main__':
    main()
