import random

from tests.support.run import run

is_anagram = run("content/strings/anagram.py")[0]["is_anagram"]
rng = random.Random(786)
for _ in range(3000):
    a = "".join(rng.choice("abc") for _ in range(rng.randint(0, 5)))
    b = "".join(rng.choice("abc") for _ in range(rng.randint(0, 5)))
    assert is_anagram(a, b) == all(a.count(c) == b.count(c) for c in "abc")
