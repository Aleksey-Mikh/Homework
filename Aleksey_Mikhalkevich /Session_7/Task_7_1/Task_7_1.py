"""
Implement class-based context manager for opening
and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor.
"""


class FilePathNotFoundError(Exception):
    """class Exception which call when raise FileNotFoundError"""

    def __init__(self, message):
        super().__init__(message)


class FileOpen:
    """
    context manager for opening
    and working with file, including handling exceptions.
    """

    def __init__(self, path, file_mode="r"):
        self.path = path
        self.file_mode = file_mode

    def __enter__(self):
        try:
            self.opened_file = open(self.path, self.file_mode)
            return self.opened_file
        except FileNotFoundError:
            raise FilePathNotFoundError(f"No such file or directory: {self.path}") from None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Resource.__exit__{(exc_type, exc_val, exc_tb)}")
        self.opened_file.close()


def main():

    with FileOpen('../tests/files/unsorted_names.txt') as file:
        data = file.readlines()

    with FileOpen("unsorted_names_w.txt", "w") as file:
        data.reverse()
        file.writelines(data)


if __name__ == '__main__':
    main()
