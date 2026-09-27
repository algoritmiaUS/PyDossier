import random

from tests.support.run import run

env = run("content/math/digits.py")[0]
rng = random.Random(788)
for _ in range(3000):
    n = rng.randint(0, 10 ** 9)
    s, r, x = 0, 0, n
    while x:
        s, r, x = s + x % 10, r * 10 + x % 10, x // 10
    assert env["digit_sum"](n) == s
    assert env["reverse_number"](n) == r
    assert env["from_binary"](env["to_binary"](n)) == n
