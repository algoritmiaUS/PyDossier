s = {3, 1, 4}
s.add(1)
s.add(5)
s.discard(3)
print(len(s), 4 in s, 3 in s)

a, b = {1, 2, 3}, {2, 3, 4}
print(a | b, a & b, a - b)

unique = len(set([1, 1, 2, 3, 3]))
empty = set()
