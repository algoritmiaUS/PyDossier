from tests.support.run import run

env, _ = run("content/input-output/read-numbers.py", "5\n3 4\n1 2 3\n2.5\n  hello  \n")
assert env["n"] == 5
assert (env["a"], env["b"]) == (3, 4)
assert env["v"] == [1, 2, 3]
assert env["x"] == 2.5
assert env["word"] == "hello"
