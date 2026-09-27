import random

from tests.support.run import run

balanced = run("content/data-structures/stack.py")[0]["balanced"]
rng = random.Random(787)
for _ in range(3000):
    s = "".join(rng.choice("()[]{}") for _ in range(rng.randint(0, 8)))
    t = s
    while any(p in t for p in ("()", "[]", "{}")):
        t = t.replace("()", "").replace("[]", "").replace("{}", "")
    assert balanced(s) == (t == "")
