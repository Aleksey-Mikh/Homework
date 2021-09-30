"""
Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator.
"""
from contextlib import contextmanager


class FilePathNotFoundError(Exception):
    """class Exception which call when raise FileNotFoundError"""

    def __init__(self, message):
        super().__init__(message)


@contextmanager
def file_open(path, file_mode="r"):
    """
    context manager for opening and working with file,
    including handling exceptions with @contextmanager decorator.
    """
    try:
        opened_file = open(path, file_mode)
        yield opened_file
    except FileNotFoundError:
        raise FilePathNotFoundError(f"No such file or directory: {path}") from None

    opened_file.close()


def main():
    with file_open('unsorted_names.txt') as file:
        data = file.readlines()

    with file_open("unsorted_names_w.txt", "w") as file:
        data.reverse()
        file.writelines(data)


if __name__ == '__main__':
    main()
