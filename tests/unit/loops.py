from tests.support.run import run

env, out = run("content/basics/loops.py")
assert out == "0 1 2 3 4 \n2 5 8 \n5 4 3 2 1 \n0 1 2 4 5 \n"
assert env["total"] == 8
assert env["digits"] == 4
