import math
import random

from tests.support.run import run

env = run("content/math/gcd-lcm.py")[0]
gcd, lcm = env["gcd"], env["lcm"]
rng = random.Random(784)
for _ in range(5000):
    a, b = rng.randint(1, 10 ** 12), rng.randint(1, 10 ** 12)
    assert gcd(a, b) == math.gcd(a, b)
    assert lcm(a, b) == math.lcm(a, b)
