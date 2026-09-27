from tests.support.run import run

sieve = run("content/math/sieve.py")[0]["sieve"]
assert sieve(1) == [False, False]
assert sieve(2) == [False, False, True]
p = sieve(30)
assert len(p) == 31
assert [i for i in range(31) if p[i]] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert sum(sieve(10 ** 6)) == 78498
