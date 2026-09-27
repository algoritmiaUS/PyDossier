from tests.support.run import run

count_components = run("content/graph/components.py")[0]["count_components"]
assert count_components([]) == 0
assert count_components([[]]) == 1
assert count_components([[], [], []]) == 3
assert count_components([[1], [0], [3], [2], []]) == 3
assert count_components([[1, 2], [0], [0]]) == 1
