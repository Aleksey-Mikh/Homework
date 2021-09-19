"""
Implement a function, that receives changeable number
of dictionaries (keys - letters, values - numbers) and combines
them into one dictionary. Dict values should be summarized
in case of identical keys
"""


def combine_dicts(*args):
    """
    function, that receives changeable number
    of dictionaries (keys - letters, values - numbers)
    and combines them into one dictionary.
    """
    result_dict = {}
    for dict_ in args:
        list_of_tuples = [(key, value) for key, value in dict_.items()]

        for tuple_for_dict in list_of_tuples:
            if tuple_for_dict[0] not in result_dict:
                result_dict[tuple_for_dict[0]] = tuple_for_dict[1]
            else:
                result_dict[tuple_for_dict[0]] += tuple_for_dict[1]

    return result_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))

print(combine_dicts(dict_1, dict_2, dict_3))
