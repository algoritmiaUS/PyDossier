import random

from tests.support.run import run

env = run("content/techniques/prefix-sums.py")[0]
prefix_sums, range_sum = env["prefix_sums"], env["range_sum"]
rng = random.Random(781)
for _ in range(1000):
    v = [rng.randint(-50, 50) for _ in range(rng.randint(1, 12))]
    p = prefix_sums(v)
    l = rng.randrange(len(v))
    r = rng.randrange(l, len(v))
    assert range_sum(p, l, r) == sum(v[l:r + 1])
