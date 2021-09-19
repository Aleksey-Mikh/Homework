"""
Implement a function which works the same as str.split method
(without using str.split itself, of course).
"""


def rebuild_split(string, sep=None):
    """function which works the same as str.split method"""
    result_list, word, check_sep = [], "", []
    ind = 0

    if sep is None:
        sep = " "
        string = list(string.strip())
    else:
        string = list(string)

    for letter in string:
        if check_sep and letter != sep[ind]:
            word += "".join(check_sep)
            ind, check_sep = 0, []

        if letter == sep[ind]:
            ind += 1
            check_sep.append(letter)
        else:
            word += letter

        if len(check_sep) == len(sep):
            result_list.append(word)
            ind, word, check_sep = 0, "", []
    if not sep.isalnum():  # if sep includes only whitespace
        result_list.append(word)
    if check_sep:
        result_list += check_sep

    return result_list


def test():
    sep = None
    string = '    sad fsd    '
    result_list = rebuild_split("    sad fsd    ")
    print("-" * 40)
    print(f"Test 1: {string=}, {sep=}")
    print("Test Passed" if string.split() == result_list else "Test Fail")

    sep = '/'
    string = '    sad fsd    '
    result_list = rebuild_split(string, sep=sep)
    print("-" * 40)
    print(f"Test 2: {string=}, {sep=}")
    print("Test Passed" if string.split(sep=sep) == result_list else "Test Fail")

    sep = ' '
    string = ' '
    result_list = rebuild_split(string, sep=sep)
    print("-" * 40)
    print(f"Test 3: {string=}, {sep=}")
    print("Test Passed" if string.split(sep=sep) == result_list else "Test Fail")

    sep = ' '
    string = '   '
    result_list = rebuild_split(string, sep=sep)
    print("-" * 40)
    print(f"Test 4: {string=}, {sep=}")
    print("Test Passed" if string.split(sep=sep) == result_list else "Test Fail")

    sep = 'na'
    string = "banan naannan"
    result_list = rebuild_split(string, sep=sep)
    print("-" * 40)
    print(f"Test 5: {string=}, {sep=}")
    print("Test Passed" if string.split(sep=sep) == result_list else "Test Fail")
    print(string.split(sep=sep), result_list)

    sep = 'tot'
    string = "tot sdf fadtot fdaf rtoot"
    result_list = rebuild_split(string, sep=sep)
    print("-" * 40)
    print(f"Test 6: {string=}, {sep=}")
    print("Test Passed" if string.split(sep=sep) == result_list else "Test Fail")
    print(string.split(sep=sep), result_list)


def main():
    test()


if __name__ == '__main__':
    main()
