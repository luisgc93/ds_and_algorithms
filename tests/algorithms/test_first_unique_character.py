import pytest
from algorithms.first_unique_character import get_unique_character


@pytest.mark.parametrize("input_string, expected_output", [
    ("statistics", 3),
    ("hackthegame", 3),
])
def test_first_unique_character(input_string, expected_output):

    assert get_unique_character(input_string) == expected_output

