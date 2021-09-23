"""
Open file data/unsorted_names.txt in data folder.
Sort the names and write them to a new file
called sorted_names.txt. Each name should start
with a new line as in the following example:
```
Adele
Adrienne
...
Willodean
Xavier
```
"""


def sort_list(unsorted_list):
    return sorted(unsorted_list)


def save_file(sorted_list):
    """save data as sorted_name.txt"""
    with open("sorted_name.txt", "w") as file:
        for name in sorted_list:
            file.write(f"{name}\n")


def open_file():
    data = []
    path = "../data/unsorted_names.txt"

    with open(path) as file:
        for line in file:
            data.append(line.strip())

    return data


def main():
    unsorted_list = open_file()
    sorted_list = sort_list(unsorted_list)
    save_file(sorted_list)


if __name__ == '__main__':
    main()
