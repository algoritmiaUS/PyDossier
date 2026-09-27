n = int(input())

if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

if 1 <= n <= 10 and n % 2 == 0:
    print("small even")

parity = "even" if n % 2 == 0 else "odd"
print(parity)
