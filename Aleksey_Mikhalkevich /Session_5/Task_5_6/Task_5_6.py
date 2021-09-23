"""
Implement a decorator call_once which runs a function or method
once and caches the result. All consecutive calls to this function
should return cached result no matter the arguments.

Examples:
```
sum_of_numbers(13, 42)
Output: 55

sum_of_numbers(999, 100)
Output: 55

sum_of_numbers(134, 412)
Output: 55
```
"""


def call_once(func):
    """
    function which runs once and caches the result.
    All consecutive calls to this function should
    return cached result no matter the arguments.
    """
    member = None

    def wrapper(*args, **kwargs):
        nonlocal member

        if member is not None:
            return member

        result = func(*args, **kwargs)
        member = result
        return result

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


def main():
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))


if __name__ == '__main__':
    main()
