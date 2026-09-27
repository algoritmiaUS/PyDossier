from tests.support.run import run

env, _ = run("content/techniques/sort.py")
assert env["v"] == [1, 2, 5, 9]
assert env["w"] == [9, 5, 2, 1]
assert env["by_len"] == ["fig", "pear", "banana"]
assert env["pairs"] == [(1, "z"), (2, "a"), (2, "b")]
assert env["people"] == [("ana", 30), ("cy", 30), ("bo", 25)]
