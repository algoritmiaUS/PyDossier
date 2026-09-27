from tests.support.run import run

env, out = run("content/strings/ord-chr.py")
shift = env["shift"]
assert out == "97 65 48\na c\n"
assert env["pos"] == 3
assert shift("a", 1) == "b" and shift("z", 1) == "a" and shift("c", -3) == "z"
assert shift("m", 26) == "m" and shift("a", 53) == "b"
