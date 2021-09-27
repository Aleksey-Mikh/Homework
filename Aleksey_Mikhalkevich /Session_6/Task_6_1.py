"""
Implement a Counter class which optionally accepts the start value
and the counter stop value. If the start value is not specified the
counter should begin with 0. If the stop value is not specified
it should be counting up infinitely. If the counter reaches
the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

If you are familiar with Exception rising use it to display
the "Maximal value is reached." message.

Example:
```
c = Counter(start=42)
c.increment()
c.get()

output: 43

c = Counter()
c.increment()
c.get()
output: 1

c = Counter(start=42, stop=43)
c.increment()
c.get()
output: 43
c.increment()
output: __main__.MaxCountException: Maximal value is reached.
```
"""


import math


class MaxCountException(Exception):
    """class exception which calls when the counter reaches the stop value"""

    def __init__(self, message):
        super().__init__(message)


class Counter:
    """
    class which optionally accepts the start value and the counter stop value.
    If the counter reaches the stop value, raise MaxCountException.
    """

    def __init__(self, start=0, stop=math.inf):
        self.start = start
        self.stop = stop

    def __str__(self):
        return f"class Counter where start value = {self.start}" \
               f" and stop value = {self.stop}"

    def increment(self):
        self._check_value()
        self.start += 1

    def get(self):
        return self.start

    def _check_value(self):
        if self.start >= self.stop:
            raise MaxCountException("Maximal value is reached.")


def main():
    c = Counter(start=42)
    print(c)
    c.increment()
    print(c.get())

    c = Counter()
    print(c)
    c.increment()
    print(c.get())

    c = Counter(start=42, stop=43)
    print(c)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())


if __name__ == '__main__':
    main()
