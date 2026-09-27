from tests.support.run import run

is_palindrome = run("content/strings/palindrome.py")[0]["is_palindrome"]
for s in ["", "a", "aa", "aba", "abba", "racecar"]:
    assert is_palindrome(s), s
for s in ["ab", "abca", "Aa", "abcab"]:
    assert not is_palindrome(s), s
