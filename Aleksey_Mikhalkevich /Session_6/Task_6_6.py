"""
A singleton is a class that allows only a single instance
of itself to be created and gives access to that created instance.
Implement singleton logic inside your custom class using a method
to initialize class instance.

Example:
```
p = Sun.inst()
f = Sun.inst()
p is f

output: True
```
"""


class Sun:
    """
    singleton is a class that allows only a single
    instance of itself to be created and gives access
    to that created instance.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)

    @staticmethod
    def inst():
        return Sun()


def main():
    p = Sun.inst()
    f = Sun.inst()
    print(p is f)


if __name__ == '__main__':
    main()
