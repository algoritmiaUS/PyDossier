from tests.support.run import run

env, out = run("content/data-structures/list.py")
assert env["v"] == [5, 8]
assert (env["last"], env["first"]) == (1, 9)
assert env["zeros"] == [0] * 5
assert env["squares"] == [0, 1, 4, 9, 16]
assert env["evens"] == [0, 2, 4, 6, 8]
assert out.splitlines() == ["2 5 8", "[8] [8, 5]", "True 1 1", "0 5", "1 8"]
