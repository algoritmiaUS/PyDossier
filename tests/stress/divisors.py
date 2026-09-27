from tests.support.run import run

divisors = run("content/math/divisors.py")[0]["divisors"]
for n in range(1, 3000):
    assert divisors(n) == [d for d in range(1, n + 1) if n % d == 0]
