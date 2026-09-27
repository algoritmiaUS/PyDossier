s = "Hello World"
print(len(s), s[0], s[-1], s[0:5])
print(s.lower(), s.upper())
print(s.split())
print(s.replace("l", "L"))
print(s.find("World"), s.find("xyz"), "lo" in s)
print(s.count("o"), s[::-1])
print("-".join(["a", "b", "c"]))
print("123".isdigit(), "abc".isalpha(), "A".isupper())

chars = list(s)
chars[0] = "J"
t = "".join(chars)
