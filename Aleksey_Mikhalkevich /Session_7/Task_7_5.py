"""
Implement function for check that number is even and is greater than 2.
Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception
(not Base Exception class).
"""


class MyBaseException(Exception):
    """custom base exception"""
    pass


class NumberIsNotNumberError(MyBaseException):
    """exception raise when number isn't a integer"""
    pass


class NumberLessThan2Error(MyBaseException):
    """exception raise when number less than 2"""
    pass


class NumberIsNotEvenError(MyBaseException):
    """exception raise when number isn't even"""
    pass


def check_number(number):
    """function for check a number is even and is greater than 2."""
    try:
        number = int(number)
    except (ValueError, TypeError):
        raise NumberIsNotNumberError(f"{number} must be integer!")

    if number <= 2:
        raise NumberLessThan2Error(f"{number} must be greater than 2!")
    elif number % 2 != 0:
        raise NumberIsNotEvenError(f"{number} must be even!")

    return True


def main():
    number = input("input a number: ")
    print(check_number(number))


if __name__ == '__main__':
    main()
