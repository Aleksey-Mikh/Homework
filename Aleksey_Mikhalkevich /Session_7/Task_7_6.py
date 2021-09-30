"""
Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program successfully close.
Use function from Task 5.5 for validating input,
handle all exceptions and print user friendly output.
"""

from Session_7.Task_7_5 import check_number


def get_set_prime_numbers(number):
    """
    function get number and return set of all
    prime number up to this one.
    """
    prime_numbers = set()

    for i in range(2, number + 1):
        for j in prime_numbers:
            if i % j == 0:
                break
        else:
            prime_numbers.add(i)

    return prime_numbers


def check_goldbachs_conjecture(number, prime_numbers):
    """find sum of prime numbers to get number"""
    for num in prime_numbers:
        if number - num in prime_numbers:
            return f"{number} = {num} + {number - num}"


def main():
    while True:
        number = input("input a number to check Goldbach's conjecture (press 'q' to exit): ")
        if number.lower() == "q":
            break
        elif check_number(number):
            number = int(number)
            prime_numbers = get_set_prime_numbers(number)
            result = check_goldbachs_conjecture(number, prime_numbers)
            print(result)
    print("The program is completed")


if __name__ == '__main__':
    main()
