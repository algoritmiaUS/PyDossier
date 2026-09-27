print(ord("a"), ord("A"), ord("0"))
print(chr(97), chr(ord("a") + 2))
pos = ord("d") - ord("a")


def shift(ch, k):
    return chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
