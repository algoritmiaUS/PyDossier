v = [4, 1, 7, 3]
print(sum(v), min(v), max(v), len(v))
print(sum(v) / len(v))
print(any(x > 5 for x in v), all(x > 1 for x in v))
print(list(range(3)), list(reversed(v)))

names = ["ana", "bo"]
for name, x in zip(names, v):
    print(name, x)
