import random

from tests.support.run import run

is_palindrome = run("content/strings/palindrome.py")[0]["is_palindrome"]
rng = random.Random(785)
for _ in range(3000):
    s = "".join(rng.choice("ab") for _ in range(rng.randint(0, 8)))
    assert is_palindrome(s) == all(s[i] == s[len(s) - 1 - i] for i in range(len(s)))
