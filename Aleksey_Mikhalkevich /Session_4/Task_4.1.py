"""
Implement a function which receives a string and
replaces all " symbols with ' and vise versa.

Examples:
```
Input: "Don't forget," said John. "As Mr. B said,
"it's mandarin, not margarine'."

Output: 'Don"t forget,' said John. 'As Mr. B said,
'it"s mandarin, not margarine".'
```
"""

QUOTATION_MARKS = {
    "\'": "\"",
    "\"": "\'",
}


def replace_quotation_marks(string):
    list_symbols = list(string)
    for n, s in enumerate(list_symbols):
        if s in QUOTATION_MARKS:
            list_symbols[n] = QUOTATION_MARKS[s]
    return "".join(list_symbols)


def main():
    string = input("input a string with various type quotation marks: ")
    new_string = replace_quotation_marks(string)
    print(new_string)


if __name__ == "__main__":
    main()
