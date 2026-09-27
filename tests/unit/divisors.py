from tests.support.run import run

divisors = run("content/math/divisors.py")[0]["divisors"]
assert divisors(1) == [1]
assert divisors(7) == [1, 7]
assert divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
assert divisors(12) == [1, 2, 3, 4, 6, 12]
