from tests.support.run import run

env, _ = run("content/techniques/binary-search.py")
contains, count_between = env["contains"], env["count_between"]
v = [1, 3, 3, 3, 7, 9]
assert contains(v, 3) and contains(v, 1) and contains(v, 9)
assert not contains(v, 0) and not contains(v, 5) and not contains(v, 10)
assert not contains([], 1)
assert count_between(v, 3, 7) == 4
assert count_between(v, 4, 6) == 0
assert count_between(v, -5, 50) == 6
