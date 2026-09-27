from tests.support.run import run

env, out = run("content/input-output/read-grid.py", "2 3\n.#.\n...\n")
assert env["grid"] == [".#.", "..."]
assert out == "#\n"
