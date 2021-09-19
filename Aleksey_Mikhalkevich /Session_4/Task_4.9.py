"""
Implement a bunch of functions which receive a changeable
number of strings and return next parameters:

    1.characters that appear in all strings

    2.characters that appear in at least one string

    3.characters that appear at least in two strings

    4.characters of alphabet, that were not used in any string

Note: use string.ascii_lowercase for list of alphabet letters
"""

import string


def get_result_find(strings):
    """function where string intersection with alphabet"""
    result_one_str, result_all_str = set(), list()
    alphabet = set(string.ascii_lowercase)

    for test_str in strings:
        result_one_str = alphabet.intersection(set(test_str))
        result_all_str.append(result_one_str)

    return result_all_str


def test_1_1(*strings):
    """function which returns characters that appear in all strings"""
    result_all_str = get_result_find(strings)
    result = result_all_str[0].intersection(*result_all_str[1:])
    return result


def test_1_2(*strings):
    """function which returns characters that appear in at least one string"""
    result_all_str = get_result_find(strings)
    result = result_all_str[0].union(*result_all_str[1:])
    return result


def test_1_3(*strings):
    """function which returns characters that appear at least in two strings"""
    dict_letters = {}
    result_all_str = get_result_find(strings)
    result_union = result_all_str[0].union(*result_all_str[1:])

    for str_test in result_all_str:
        for letter in result_union:

            if letter in str_test:
                if letter not in dict_letters:
                    dict_letters[letter] = 1
                else:
                    dict_letters[letter] += 1

    filtered_tuple = filter(lambda x: x[1] >= 2, dict_letters.items())
    filtered_dict = dict(filtered_tuple)
    return set(filtered_dict.keys())


def test_1_4(*strings):
    """
    function which returns characters of alphabet,
    that were not used in any string
    """
    result_all_str = get_result_find(strings)
    alphabet = set(string.ascii_lowercase)
    result = alphabet.difference(*result_all_str)
    return result


def main():
    test_strings = eval(
        input("input a list of elements in format - [\"hello\", \"world\", \"python\"]: ")
    )
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings))


if __name__ == '__main__':
    main()
