from bisect import bisect_left, bisect_right


def contains(v, x):
    i = bisect_left(v, x)
    return i < len(v) and v[i] == x


def count_between(v, lo, hi):
    return bisect_right(v, hi) - bisect_left(v, lo)
