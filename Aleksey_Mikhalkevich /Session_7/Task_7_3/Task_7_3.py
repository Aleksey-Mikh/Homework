"""
Implement decorator with context manager support
for writing execution time to log-file. See contextlib module.
"""

import time
from contextlib import ContextDecorator
import logging

logging.basicConfig(filename="example.log", filemode="w", level=logging.INFO)


class track_entry_and_exit(ContextDecorator):
    """
    decorator with context manager support for
    writing execution time to log-file.
    """
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.time_start = time.time()
        logging.info(f"Entering: {self.name}")

    def __exit__(self, exc_type, exc, exc_tb):
        self.time_end = time.time()
        logging.info(f"Exiting: {self.name}, execution time: {self.time_end - self.time_start:.2f} seconds")


@track_entry_and_exit("func - activity")
def activity():
    time.sleep(5)


def main():
    activity()


if __name__ == '__main__':
    main()
