v = [1, 2, 3]
print(*v)
print(" ".join(map(str, v)))
print(*v, sep="\n")
print("a", "b", sep="")
print("no newline", end="")
print()

x = 3.14159
print(f"{x:.2f}")
print(f"Case #{1}: {x:.3f}")
print("YES" if len(v) > 2 else "NO")

out = [str(i * i) for i in range(4)]
print("\n".join(out))
