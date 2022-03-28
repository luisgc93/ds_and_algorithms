import pytest

from algorithms.palindrome_number import is_palindrome, is_palindrome_without_string_conversion


@pytest.mark.parametrize("number, expected_result", [
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (456654, True),
    (1, True),
])
def test_is_palindrome(number, expected_result):
    assert is_palindrome(number) == expected_result
    assert is_palindrome_without_string_conversion(number) == expected_result
