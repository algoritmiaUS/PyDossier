from tests.support.run import run

env, out = run("content/math/gcd-lcm.py")
gcd, lcm = env["gcd"], env["lcm"]
assert out == "6 12\n"
assert gcd(12, 18) == 6 and gcd(7, 13) == 1 and gcd(0, 5) == 5 and gcd(5, 0) == 5
assert lcm(4, 6) == 12 and lcm(1, 9) == 9 and lcm(10 ** 18, 3) == 3 * 10 ** 18
