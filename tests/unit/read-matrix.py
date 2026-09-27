from tests.support.run import run

env, out = run("content/input-output/read-matrix.py", "2 3\n1 2 3\n4 5 6\n")
assert env["a"] == [[1, 2, 3], [4, 5, 6]]
assert out == "6\n"
