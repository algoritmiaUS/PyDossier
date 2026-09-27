from tests.support.run import run

env, _ = run("content/input-output/read-all.py", "4\n1 2\n3\n\n4\n")
assert env["n"] == 4
assert env["v"] == [1, 2, 3, 4]
