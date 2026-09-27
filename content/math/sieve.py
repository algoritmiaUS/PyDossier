import math


def sieve(n):
    prime = [False, False] + [True] * (n - 1)
    for i in range(2, math.isqrt(n) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime
