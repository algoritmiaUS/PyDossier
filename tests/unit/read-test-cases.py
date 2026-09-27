from tests.support.run import run

_, out = run("content/input-output/read-test-cases.py", "3\n2\n1 2\n1\n5\n3\n-1 1 1\n")
assert out == "3\n5\n1\n"
