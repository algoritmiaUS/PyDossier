from tests.support.run import run

sieve = run("content/math/sieve.py")[0]["sieve"]
is_prime = run("content/math/is-prime.py")[0]["is_prime"]
for n in range(1, 300):
    assert sieve(n) == [is_prime(i) for i in range(n + 1)]
