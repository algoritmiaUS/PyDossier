from tests.support.run import run

assert run("content/input-output/read-until-eof.py", "1 2\n10 -3\n5 5")[1] == "3\n7\n10\n"
assert run("content/input-output/read-until-eof.py", "")[1] == ""
