from tests.support.run import run

is_prime = run("content/math/is-prime.py")[0]["is_prime"]
for n in range(-5, 3000):
    assert is_prime(n) == (n >= 2 and all(n % d for d in range(2, n)))
