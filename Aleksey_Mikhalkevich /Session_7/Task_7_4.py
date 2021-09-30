"""
Implement decorator for suppressing exceptions.
If exception not occurred write log to console.
"""

import logging

logging.basicConfig(level=logging.INFO)


def suppressing_exceptions(func):
    """
    decorator for suppressing exceptions.
    If exception not occurred write log to console.
    """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"Exception wasn't raised")
            return result
        except Exception:
            pass

    return wrapper


@suppressing_exceptions
def raise_exceptions(flag):
    if flag:
        raise Exception


def main():
    raise_exceptions(True)
    raise_exceptions(False)


if __name__ == '__main__':
    main()
