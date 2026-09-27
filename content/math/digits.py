def digit_sum(n):
    return sum(int(d) for d in str(n))


def reverse_number(n):
    return int(str(n)[::-1])


def to_binary(n):
    return bin(n)[2:]


def from_binary(s):
    return int(s, 2)
