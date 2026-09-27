from tests.support.run import run

cases = {
    "7\n": ["positive", "odd"],
    "4\n": ["positive", "small even", "even"],
    "12\n": ["positive", "even"],
    "0\n": ["zero", "even"],
    "-3\n": ["negative", "odd"],
}
for stdin, want in cases.items():
    assert run("content/basics/conditionals.py", stdin)[1].splitlines() == want
