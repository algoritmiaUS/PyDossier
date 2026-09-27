from tests.support.run import run

env, out = run("content/techniques/brute-force.py")
assert out.splitlines() == [
    "[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]",
    "[(1, 2), (1, 3), (2, 3)]",
    "[(0, 0), (0, 1), (1, 0), (1, 1)]",
]
subsets_with_sum = env["subsets_with_sum"]
assert subsets_with_sum([], 0) == 1
assert subsets_with_sum([1, 2, 3], 3) == 2
assert subsets_with_sum([2, 2, 2], 4) == 3
assert subsets_with_sum([5], 1) == 0
