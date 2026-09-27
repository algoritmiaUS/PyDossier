from tests.support.run import run

balanced = run("content/data-structures/stack.py")[0]["balanced"]
for s in ["", "()", "([]{})", "(()[{}])", "{[()()]}"]:
    assert balanced(s), s
for s in ["(", ")", "(]", "([)]", "(()", "())", "}{"]:
    assert not balanced(s), s
