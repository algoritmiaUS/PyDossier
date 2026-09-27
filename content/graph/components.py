def count_components(g):
    seen = [False] * len(g)
    count = 0
    for s in range(len(g)):
        if seen[s]:
            continue
        count += 1
        seen[s] = True
        stack = [s]
        while stack:
            u = stack.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
    return count
