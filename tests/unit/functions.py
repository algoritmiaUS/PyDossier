from tests.support.run import run

env, out = run("content/basics/functions.py")
assert out == "5 Hello, world! Hello, Ana! 2 9\n"
assert env["min_max"]([7]) == (7, 7)
assert [env["factorial"](n) for n in range(6)] == [1, 1, 2, 6, 24, 120]
