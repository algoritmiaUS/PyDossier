import random

from tests.support.graphs import random_graph
from tests.support.run import run

bfs = run("content/graph/bfs.py")[0]["bfs"]
rng = random.Random(777)
INF = float("inf")
for _ in range(1000):
    n = rng.randint(1, 8)
    g = random_graph(rng, n)
    d = [[0 if i == j else 1 if j in g[i] else INF for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    s = rng.randrange(n)
    assert bfs(g, s) == [-1 if x == INF else x for x in d[s]]
