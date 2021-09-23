"""
Implement a decorator remember_result which
remembers last result of function it decorates
and prints it before next call.

Examples:
```
sum_list("a", "b")
Output:
    "Last result = 'None'"
    "Current result = 'ab'"

sum_list("abc", "cde")
Output:
    "Last result = 'ab'"
    "Current result = 'abccde'"
```
"""


def remember_result_v2(func):
    """another realization remember_result"""

    def wrapper(*args, last_result=[None], **kwargs):
        print(f"Last result = {last_result[0]}")
        current_result = func(*args, **kwargs)
        last_result[0] = current_result
        return current_result
    return wrapper


def remember_result(func):
    """
    decorator which remembers last result of function
    it decorates and prints it before next call.
    """
    last_result = None

    def wrapper(*args, **kwargs):
        nonlocal last_result
        print(f"Last result = {last_result}")
        current_result = func(*args, **kwargs)
        last_result = current_result
        return current_result
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    try:
        for item in args:
            result += item
    except TypeError:
        result = str(sum(args))
    print(f"Current result = '{result}'")
    return result


def main():
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)


if __name__ == '__main__':
    main()
