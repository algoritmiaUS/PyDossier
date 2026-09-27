from tests.support.run import run

env, out = run("content/data-structures/dict.py")
assert env["age"] == {"ana": 21, "eva": 30}
assert env["count"] == {"a": 3, "b": 1, "c": 1}
assert out.splitlines() == ["21 3", "0 True", "ana 21", "eva 30"]
