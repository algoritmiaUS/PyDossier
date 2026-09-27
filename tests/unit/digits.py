from tests.support.run import run

env, _ = run("content/math/digits.py")
assert env["digit_sum"](0) == 0 and env["digit_sum"](9875) == 29
assert env["reverse_number"](1230) == 321 and env["reverse_number"](7) == 7
assert env["to_binary"](0) == "0" and env["to_binary"](10) == "1010"
assert env["from_binary"]("1010") == 10 and env["from_binary"]("0") == 0
