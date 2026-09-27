from collections import Counter

c = Counter("banana")
print(c["a"], c["z"])
print(c.most_common(2))

v = Counter([3, 1, 3, 2, 3])
print(max(v, key=v.get))
