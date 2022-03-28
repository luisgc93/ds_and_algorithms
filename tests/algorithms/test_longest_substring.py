import pytest

from algorithms.longest_substring import length_of_longest_substring_brute_force, length_of_longest_substring_optimized


@pytest.mark.parametrize("string, expected_result", [
    ("abcabcbb", 3),
    ("abccbcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    (" ", 1),
    ("a", 1),
    ("aab", 2),
    ("dvdf", 3),
])
def test_longest_substring(string, expected_result):
    assert length_of_longest_substring_brute_force(string) == expected_result
    assert length_of_longest_substring_optimized(string) == expected_result
