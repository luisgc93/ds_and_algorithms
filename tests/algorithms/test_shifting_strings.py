import pytest
from algorithms.shifting_strings import get_shifted_string_original_version, \
    get_shifted_string_improved, get_shifted_string_best_version


@pytest.mark.parametrize("string, left_shift, right_shift, expected", [
    ("abcdef", 10, 8, "cdefab"),
    ("abcdefghijklmnopqrst", 10, 10, "abcdefghijklmnopqrst"),
    ("abcdefghijklmnopqrst", 4, 19, "fghijklmnopqrstabcde"),
    ("abcdefghijklmnopqrst", 60, 20, "abcdefghijklmnopqrst"),
])
def test_shift_strings(string, left_shift, right_shift, expected):
    assert get_shifted_string_original_version(string, left_shift, right_shift) == expected
    assert get_shifted_string_improved(string, left_shift, right_shift) == expected
    assert get_shifted_string_best_version(string, left_shift, right_shift) == expected
