import heapq

from tests.support.run import run

env, _ = run("content/data-structures/heap.py")
assert (env["smallest"], env["x"]) == (1, 1)
assert sorted(env["h"]) == [3, 5]
assert env["v"][0] == 2
assert [heapq.heappop(env["v"]) for _ in range(3)] == [2, 4, 7]
assert env["largest"] == 9
