from tests.support.run import run

env, _ = run("content/graph/read-graph.py", "4 3\n1 2\n2 3\n1 3\n")
assert env["g"] == [[1, 2], [0, 2], [1, 0], []]
assert run("content/graph/read-graph.py", "1 0\n")[0]["g"] == [[]]
