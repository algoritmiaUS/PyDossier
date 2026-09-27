from tests.support.run import run

dfs = run("content/graph/dfs.py")[0]["dfs"]
assert dfs([[]], 0) == [True]
assert dfs([[1], [0], []], 0) == [True, True, False]
assert dfs([[1], [0], [3], [2]], 3) == [False, False, True, True]
n = 10 ** 5
line = [[i - 1, i + 1] for i in range(n)]
line[0], line[-1] = [1], [n - 2]
assert all(dfs(line, 0))
