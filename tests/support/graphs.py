def random_graph(rng, n):
    g = [[] for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < 0.3:
                g[u].append(v)
                g[v].append(u)
    return g


def reachable(g):
    n = len(g)
    r = [[i == j or j in g[i] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                r[i][j] = r[i][j] or (r[i][k] and r[k][j])
    return r
