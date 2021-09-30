"""
Implement a generator which will generate Fibonacci numbers endlessly.
"""

import time


def endless_fib_generator():
    """generator which will generate Fibonacci numbers endlessly."""
    previous = 0
    current = 1
    while True:
        yield current
        previous, current = current, previous + current


def main():
    gen = endless_fib_generator()
    while True:
        print(next(gen))
        time.sleep(0.5)  # sleep for normal output


if __name__ == '__main__':
    main()
