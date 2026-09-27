from tests.support.run import run

bfs = run("content/graph/bfs.py")[0]["bfs"]
assert bfs([[]], 0) == [0]
assert bfs([[1], [0, 2], [1]], 0) == [0, 1, 2]
assert bfs([[1], [0], []], 0) == [0, 1, -1]
assert bfs([[1, 2], [0, 2], [0, 1]], 0) == [0, 1, 1]
