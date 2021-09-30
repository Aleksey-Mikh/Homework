"""
Implement a generator which will generate odd numbers endlessly.
"""

import time


def endless_generator():
    """generator which will generate odd numbers endlessly."""
    number = 1
    while True:
        yield number
        number += 2


def main():
    gen = endless_generator()
    while True:
        print(next(gen))
        time.sleep(0.5)  # sleep for normal output


if __name__ == '__main__':
    main()
