def add(a, b):
    return a + b


def greet(name="world"):
    return f"Hello, {name}!"


def min_max(v):
    return min(v), max(v)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


lo, hi = min_max([4, 2, 9])
print(add(2, 3), greet(), greet("Ana"), lo, hi)
