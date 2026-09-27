from itertools import combinations, permutations, product

v = [1, 2, 3]
print(list(permutations(v)))
print(list(combinations(v, 2)))
print(list(product([0, 1], repeat=2)))


def subsets_with_sum(v, target):
    count = 0
    for take in product([False, True], repeat=len(v)):
        s = sum(x for x, t in zip(v, take) if t)
        count += s == target
    return count
