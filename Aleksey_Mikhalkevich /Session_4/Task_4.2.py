"""
Write a function that check whether a string is a palindrome or not.
Usage of any reversing functions is prohibited.

Examples:
```
Input: Mr. Owl ate my metal worm
Output: String is a palindrome
```
"""
import re


def get_clear_string(string):
    """Remove all characters except letters and numbers"""
    template = r"[^A-Za-z0-9]"
    string = re.sub(template, "", string)
    return string


def find_palindrome(string):
    if string == string[::-1]:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")


def main():
    string = input("input a string to check if it is a palindrome: ")
    string = get_clear_string(string)
    find_palindrome(string.lower())


if __name__ == '__main__':
    main()
