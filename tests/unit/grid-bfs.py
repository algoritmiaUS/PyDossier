from tests.support.run import run

grid_bfs = run("content/graph/grid-bfs.py")[0]["grid_bfs"]
assert grid_bfs(["."], 0, 0) == [[0]]
assert grid_bfs(["..", ".."], 0, 0) == [[0, 1], [1, 2]]
assert grid_bfs([".#.", ".#.", "..."], 0, 0) == [[0, -1, 6], [1, -1, 5], [2, 3, 4]]
assert grid_bfs([".#", "#."], 0, 0) == [[0, -1], [-1, -1]]
