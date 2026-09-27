def divisors(n):
    small, big = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                big.append(n // i)
        i += 1
    return small + big[::-1]
