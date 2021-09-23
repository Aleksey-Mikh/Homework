"""
Implement a function which search for most common
words in the file. Use data/lorem_ipsum.txt file as a example.
"""

import string


def open_file(path):
    data = []

    with open(path) as file:
        for line in file:
            data.extend(line.strip().split())

    return data


def get_dictionary_words(data):
    """
    the function get data then removes punctuation marks
    and returns a dictionary
    where the key is a word from the data,
    and the value is how many times the word was repeated.
    """
    dictionary = {}

    for word in data:
        word = word.strip(string.punctuation).lower()
        dictionary[word] = dictionary.get(word, 0) + 1

    return dictionary


def most_common_words(filepath, number_of_words=3):
    """function which search for most common words in the file."""
    data = open_file(filepath)
    dictionary = get_dictionary_words(data)

    sorted_tuple = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)  # sorting by count of words
    result = [i[0] for i in sorted_tuple[:number_of_words]]  # make list of names

    return result


def main():
    path = "../data/lorem_ipsum.txt"
    result = most_common_words(path)
    print(result)


if __name__ == '__main__':
    main()
