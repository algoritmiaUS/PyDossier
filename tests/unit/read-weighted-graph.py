from tests.support.run import run

env, _ = run("content/graph/read-weighted-graph.py", "3 2\n1 2 5\n3 2 7\n")
assert env["g"] == [[(1, 5)], [(0, 5), (2, 7)], [(1, 7)]]
