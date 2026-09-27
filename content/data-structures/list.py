v = [5, 3, 8]
v.append(1)
v.insert(0, 9)
last = v.pop()
first = v.pop(0)
v.remove(3)
print(len(v), v[0], v[-1])
print(v[1:], v[::-1])
print(8 in v, v.index(8), v.count(5))

zeros = [0] * 5
squares = [i * i for i in range(5)]
evens = [x for x in range(10) if x % 2 == 0]

for i, x in enumerate(v):
    print(i, x)
