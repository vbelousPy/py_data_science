import math


def foo(a, b=0, c=0):
    x1 = lambda a, b, c: (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = lambda a, b, c: (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    return x1(a, b, c), x2(a, b, c)


x1, x2 = foo(1, -6, 5)
print("x1 =", x1)
print("x2 =", x2)
