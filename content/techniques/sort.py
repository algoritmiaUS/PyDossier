v = [5, 2, 9, 1]
v.sort()
w = sorted(v, reverse=True)

words = ["pear", "fig", "banana"]
by_len = sorted(words, key=len)

pairs = [(2, "b"), (1, "z"), (2, "a")]
pairs.sort()

people = [("ana", 30), ("bo", 25), ("cy", 30)]
people.sort(key=lambda p: (-p[1], p[0]))
