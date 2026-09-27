from tests.support.run import run

env, out = run("content/basics/operators.py")
assert out.splitlines() == [
    "22 12 85",
    "3.4",
    "3 2",
    "-4 3",
    f"289 {2 ** 100}",
    "857",
    "False True False True",
    "True True False",
    "3 2 3.14",
    "7",
]
