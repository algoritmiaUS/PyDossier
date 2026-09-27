import math

print(math.gcd(12, 18), math.lcm(4, 6))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b
