import random

from tests.support.graphs import random_graph, reachable
from tests.support.run import run

count_components = run("content/graph/components.py")[0]["count_components"]
rng = random.Random(779)
for _ in range(1000):
    n = rng.randint(0, 8)
    g = random_graph(rng, n)
    r = reachable(g)
    want = sum(1 for i in range(n) if not any(r[i][j] for j in range(i)))
    assert count_components(g) == want
