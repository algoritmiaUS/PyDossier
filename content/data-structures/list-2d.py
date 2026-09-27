n, m = 3, 4
good = [[0] * m for _ in range(n)]
bad = [[0] * m] * n
good[0][0] = 1
bad[0][0] = 1
print(good[1][0], bad[1][0])

rows, cols = len(good), len(good[0])
for r in range(rows):
    for c in range(cols):
        good[r][c] = r * cols + c
