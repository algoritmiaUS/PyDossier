import random

from tests.support.graphs import random_graph, reachable
from tests.support.run import run

dfs = run("content/graph/dfs.py")[0]["dfs"]
rng = random.Random(778)
for _ in range(1000):
    n = rng.randint(1, 8)
    g = random_graph(rng, n)
    s = rng.randrange(n)
    assert dfs(g, s) == reachable(g)[s]
