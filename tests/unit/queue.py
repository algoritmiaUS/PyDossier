from collections import deque

from tests.support.run import run

env, out = run("content/data-structures/queue.py")
assert (env["front"], env["x"], env["y"]) == (1, 1, 2)
assert env["q"] == deque([0])
assert out == "1 2 1\n"
