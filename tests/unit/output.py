from tests.support.run import run

_, out = run("content/input-output/output.py")
assert out.splitlines() == [
    "1 2 3",
    "1 2 3",
    "1",
    "2",
    "3",
    "ab",
    "no newline",
    "3.14",
    "Case #1: 3.142",
    "YES",
    "0",
    "1",
    "4",
    "9",
]
