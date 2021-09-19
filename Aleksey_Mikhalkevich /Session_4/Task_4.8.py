"""
Implement a function get_pairs(lst: List) -> List[Tuple]
which returns a list of tuples containing pairs of elements.
Pairs should be formed as in the example. If there is only one
element in the list return None instead.

Examples:
```
Input: [1, 2, 3, 8, 9]
Output: [(1, 2), (2, 3), (3, 8), (8, 9)]
```
"""


def get_pairs(list_numbers):
    """
    function which returns a list of tuples
    containing pairs of elements.
    """
    result = []

    for n, number in enumerate(list_numbers):
        if n == 0:  # skip first iteration
            continue
        result.append((list_numbers[n-1], number))

    return result


def check_list(list_numbers):
    if len(list_numbers) > 1:
        return True


def main():
    list_numbers = eval(
        input("input a list of elements in format - [1, 2, 3, 8, 9]: ")
    )
    if check_list(list_numbers):
        result = get_pairs(list_numbers)
        print(result)
    else:
        print(None)


if __name__ == '__main__':
    main()
