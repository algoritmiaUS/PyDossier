import random

from tests.support.run import run

subsets_with_sum = run("content/techniques/brute-force.py")[0]["subsets_with_sum"]
rng = random.Random(783)
for _ in range(500):
    v = [rng.randint(0, 6) for _ in range(rng.randint(0, 8))]
    target = rng.randint(0, 20)
    ways = [1] + [0] * target
    for x in v:
        for s in range(target, x - 1, -1):
            ways[s] += ways[s - x]
    assert subsets_with_sum(v, target) == ways[target]
