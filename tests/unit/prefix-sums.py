from tests.support.run import run

env, _ = run("content/techniques/prefix-sums.py")
prefix_sums, range_sum = env["prefix_sums"], env["range_sum"]
assert prefix_sums([]) == [0]
p = prefix_sums([3, -1, 4, 1, 5])
assert p == [0, 3, 2, 6, 7, 12]
assert range_sum(p, 0, 4) == 12
assert range_sum(p, 1, 1) == -1
assert range_sum(p, 1, 3) == 4
