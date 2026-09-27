from tests.support.run import run

env, out = run("content/basics/variables.py")
assert (env["x"], env["y"], env["s"], env["b"]) == (42, 3.5, "123", False)
assert out.splitlines()[1] == "2 1"
