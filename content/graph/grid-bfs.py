from collections import deque


def grid_bfs(grid, sr, sc):
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = r + dr, c + dc
            if not (0 <= x < n and 0 <= y < m):
                continue
            if grid[x][y] == "#" or dist[x][y] != -1:
                continue
            dist[x][y] = dist[r][c] + 1
            q.append((x, y))
    return dist
