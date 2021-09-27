from functools import total_ordering


def check_instance(func):

    def wrapper(self, other):
        if not isinstance(other, Money):
            other = Money(other)

        return func(self, other)

    return wrapper


@total_ordering
class Money:
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "USD": 1,
        "JPY": 110.14
    }

    def __init__(self, value, currency="USD"):
        self.value = value
        self.currency = currency

    def converter_currency(self):
        return self.value / self.exchange_rate[self.currency]

    @check_instance
    def __add__(self, other):
        result_sum = self.value + other.converter_currency() * self.exchange_rate[self.currency]
        result_round = round(result_sum, 2)
        return Money(result_round, self.currency)

    @check_instance
    def __radd__(self, other):
        if other == 0:
            return self
        result_sum = other.value + self.converter_currency() * self.exchange_rate[other.currency]
        result_round = round(result_sum, 2)
        return Money(result_round, other.currency)

    @check_instance
    def __sub__(self, other):
        result_sum = self.value - other.converter_currency() * self.exchange_rate[self.currency]
        result_round = round(result_sum, 2)
        return Money(result_round, self.currency)

    @check_instance
    def __rsub__(self, other):
        result_sum = other.value - self.converter_currency() * self.exchange_rate[other.currency]
        result_round = round(result_sum, 2)
        return Money(result_round, other.currency)

    @check_instance
    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError
        return Money(round(self.value / other.value, 2))

    @check_instance
    def __rtruediv__(self, other):
        if self.value == 0:
            raise ZeroDivisionError
        return Money(round(other.value / self.value, 2))

    @check_instance
    def __mul__(self, other):
        return Money(round(self.value * other.value, 2))

    @check_instance
    def __rmul__(self, other):
        return Money(round(other.value * self.value, 2))

    def __lt__(self, other):
        return self.value < other

    @check_instance
    def __eq__(self, other):
        return self.value == other.value and self.currency == other.currency

    def __str__(self):
        return f"{self.value} {self.currency}"

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value}, currency={self.currency!r})"


d = Money(15)
b = Money(10, "BYN")
e = Money(20, "EUR")
print(e - 10)
# x = Money(10, "BYN")
# z = Money(5, "EUR")
# p = Money(3)
# lst = [x, z]
# print(p + z)
# print(3 + z)
# print(z + 3)
# print(x + 3 + z)
# print(2 + x + z + 5)
# print(x + 10 + 9)
# print(sum(lst))
# print()
# print((x - z))
# print((x - 5))
# print((11 - x))
# print()
# print((x / z))
# print((x / 5), 'x / 5')
# print((20 / x), '10 / x')
# print()
# print((x * z))
# print((x * 5))
# print((11 * x))
# print()
# print(x > z)
# print(x >= z)
# print(x <= z)
# print(x < z)
# print(x == z)
# print(x != z)
# print()
# print(x > 2)
# print(x >= 3)
# print(x <= 3)
# print(x < 3)
# print(x == 3)
# print(x != 3)
# print()
# print(2 > x)
# print(2 >= x)
# print(2 <= x)
# print(2 < x)
# print(2 == x)
# print(2 != x)
# print()
# x = Money(10, "BYN")
# y = Money(11)
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8)
# print()
lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s, "las")

x, y, z = Money(10, "BYN"), Money(11), Money(12.01, "JPY")
print(x + y + z, "xyz")

print()
y = Money(50)
z = Money(50, "EUR")
print(z + y)
print(y + z)
