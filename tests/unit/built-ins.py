from tests.support.run import run

_, out = run("content/techniques/built-ins.py")
assert out.splitlines() == [
    "15 1 7 4",
    "3.75",
    "True False",
    "[0, 1, 2] [3, 7, 1, 4]",
    "ana 4",
    "bo 1",
]
