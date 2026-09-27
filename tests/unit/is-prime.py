from tests.support.run import run

is_prime = run("content/math/is-prime.py")[0]["is_prime"]
assert [n for n in range(-3, 30) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert is_prime(1_000_000_007)
assert not is_prime(1_000_000_007 * 3)
