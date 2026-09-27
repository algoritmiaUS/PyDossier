from tests.support.run import run

env, out = run("content/data-structures/counter.py")
assert dict(env["c"]) == {"b": 1, "a": 3, "n": 2}
assert out.splitlines() == ["3 0", "[('a', 3), ('n', 2)]", "3"]
