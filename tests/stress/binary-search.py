import random

from tests.support.run import run

env = run("content/techniques/binary-search.py")[0]
contains, count_between = env["contains"], env["count_between"]
rng = random.Random(782)
for _ in range(2000):
    v = sorted(rng.randint(0, 20) for _ in range(rng.randint(0, 10)))
    x = rng.randint(-2, 22)
    lo, hi = sorted((rng.randint(-2, 22), rng.randint(-2, 22)))
    assert contains(v, x) == (x in v)
    assert count_between(v, lo, hi) == sum(lo <= y <= hi for y in v)
