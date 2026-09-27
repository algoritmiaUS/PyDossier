def dfs(g, s):
    seen = [False] * len(g)
    seen[s] = True
    stack = [s]
    while stack:
        u = stack.pop()
        for v in g[u]:
            if not seen[v]:
                seen[v] = True
                stack.append(v)
    return seen
