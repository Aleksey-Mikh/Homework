"""
Implement a function that takes a number as an argument
and returns a dictionary, where the key is a number
and the value is the square of that number.

Examples:
```
Input: 5
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
"""


def generate_squares(number):
    """
    function that takes a number as an argument
    and returns a dictionary, where the key is a number
    and the value is the square of that number.
    """
    list_of_tuple = [(x, x * x) for x in range(1, number + 1)]
    return dict(list_of_tuple)


def main():
    number = int(input("input a number: "))
    dict_of_numbers = generate_squares(number)
    print(dict_of_numbers)


if __name__ == '__main__':
    main()
