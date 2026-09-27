import random

from tests.support.run import run

grid_bfs = run("content/graph/grid-bfs.py")[0]["grid_bfs"]
rng = random.Random(780)
for _ in range(500):
    n, m = rng.randint(1, 5), rng.randint(1, 5)
    grid = ["".join(rng.choice("..#") for _ in range(m)) for _ in range(n)]
    sr, sc = rng.randrange(n), rng.randrange(m)
    grid[sr] = grid[sr][:sc] + "." + grid[sr][sc + 1:]
    want = [[-1] * m for _ in range(n)]
    want[sr][sc] = 0
    changed = True
    while changed:
        changed = False
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "#":
                    continue
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < n and 0 <= y < m and want[x][y] >= 0:
                        if want[r][c] == -1 or want[x][y] + 1 < want[r][c]:
                            want[r][c] = want[x][y] + 1
                            changed = True
    assert grid_bfs(grid, sr, sc) == want
