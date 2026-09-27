from tests.support.run import run

env, out = run("content/data-structures/set.py")
assert env["s"] == {1, 4, 5}
assert env["unique"] == 3
assert env["empty"] == set()
assert out.splitlines() == ["3 True False", "{1, 2, 3, 4} {2, 3} {1}"]
