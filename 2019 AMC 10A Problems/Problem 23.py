import math
import sys

sys.setrecursionlimit(1000000)


def diamond(a, b):
    return pow(a, math.log(b, 7))


def heart(a, b):
    return pow(a, 1 / (math.log(b, 7)))


def a_function(n):
    if n == 3:
        return heart(3, 2)
    elif n >= 4:
        return diamond((heart(n, n - 1)), a_function(n - 1))


print(math.log(a_function(2019), 7))
print(round(math.log(a_function(2019), 7)))
