for i in range(5):
    print(i, end=" ")
print()

for i in range(2, 10, 3):
    print(i, end=" ")
print()

for i in range(5, 0, -1):
    print(i, end=" ")
print()

total = 0
for x in [3, 1, 4]:
    total += x

n = 3700
digits = 0
while n > 0:
    n //= 10
    digits += 1

for i in range(10):
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end=" ")
print()
