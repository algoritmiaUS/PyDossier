from tests.support.run import run

env, out = run("content/data-structures/list-2d.py")
assert out == "0 1\n"
assert env["good"] == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
assert all(row is env["bad"][0] for row in env["bad"])
