"""
Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
which splits the s string by indexes specified in indexes.
Wrong indexes must be ignored.

Examples:
```
Input: "pythoniscool,isn'tit?", [6, 8, 12, 13, 18]
Output: ['python', 'is', 'cool', ',', "isn't", 'it?']
```
"""


def split_by_index(s: str, indexes: list[int]):
    """
    function which splits the s string by indexes
    specified in indexes. Wrong indexes must be ignored.
    """
    result_list, old_index = [], 0

    for new_index in indexes:
        if new_index > len(s):
            break
        result_list.append(s[old_index:new_index])
        old_index = new_index

    result_list.append(s[old_index:])
    return result_list


def main():
    string = input("input a string: ")
    indexes = eval(input("input indexes in format - [6, 8, 12, 13, 18]: "))
    result_list = split_by_index(string, indexes)
    print(result_list)


if __name__ == '__main__':
    main()
