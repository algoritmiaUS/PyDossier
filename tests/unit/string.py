from tests.support.run import run

env, out = run("content/strings/string.py")
assert env["t"] == "Jello World"
assert out.splitlines() == [
    "11 H d Hello",
    "hello world HELLO WORLD",
    "['Hello', 'World']",
    "HeLLo WorLd",
    "6 -1 True",
    "2 dlroW olleH",
    "a-b-c",
    "True True True",
]
