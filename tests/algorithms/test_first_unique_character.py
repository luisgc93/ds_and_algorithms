import pytest
from algorithms.first_unique_character import get_unique_character


@pytest.mark.parametrize("input_string, expected_output", [
    ("statistics", 3),
    ("hackthegame", 3),
])
def test_first_unique_character(input_string, expected_output):

    assert get_unique_character(input_string) == expected_output


def test_first_unique_character_big_input():
    input_string = "a" + "s" * 60_000 + "z" + "a" + "b" * 160_000
    assert get_unique_character(input_string) == 60_002
