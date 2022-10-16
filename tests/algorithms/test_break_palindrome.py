import pytest

from algorithms.break_palindrome import break_palindrome


@pytest.mark.parametrize("palindrome_str, result", [
    ("aaabbaaa", "aaaabaaa"),
    ("bab", "aab"),
    ("aaa", "IMPOSSIBLE"),
    ("acca", "aaca"),
])
def test_break_palindrome(palindrome_str, result):

    assert break_palindrome(palindrome_str) == result
