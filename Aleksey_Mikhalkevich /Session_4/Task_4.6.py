"""
Implement a function get_shortest_word(s: str) -> str
which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on).
If there are multiple longest words in the string
with a same length return the word that occures first.


Examples:
```
Input: Python is simple and effective!
Output: effective!
```
"""


def get_shortest_word(string):
    """function which returns the longest word in the given string"""
    lst = string.split()
    max_word = max(lst, key=lambda x: len(x))
    return max_word


def main():
    string = input("input a string: ")
    longest_word = get_shortest_word(string)
    print(longest_word)


if __name__ == "__main__":
    main()
