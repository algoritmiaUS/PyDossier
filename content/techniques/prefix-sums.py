def prefix_sums(v):
    p = [0] * (len(v) + 1)
    for i, x in enumerate(v):
        p[i + 1] = p[i] + x
    return p


def range_sum(p, l, r):
    return p[r + 1] - p[l]
