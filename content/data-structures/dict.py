age = {"ana": 20, "luis": 25}
age["eva"] = 30
age["ana"] += 1
print(age["ana"], len(age))
print(age.get("bob", 0), "luis" in age)
del age["luis"]
for name, a in age.items():
    print(name, a)

count = {}
for w in "a b a c a".split():
    count[w] = count.get(w, 0) + 1
