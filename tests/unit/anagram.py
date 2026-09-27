from tests.support.run import run

is_anagram = run("content/strings/anagram.py")[0]["is_anagram"]
assert is_anagram("", "")
assert is_anagram("listen", "silent")
assert is_anagram("aab", "aba")
assert not is_anagram("aab", "abb")
assert not is_anagram("ab", "abc")
