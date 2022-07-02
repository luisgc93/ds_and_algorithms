import pytest

from algorithms.integer_to_roman import (
    integer_to_roman,
    _split_into_powers_of_10, # noqa
    _find_closest_number_that_has_its_own_character # noqa
)


def test_split_into_powers_of_10():
    assert _split_into_powers_of_10(965) == [(9, 100), (6, 10), (5, 1)]


@pytest.mark.parametrize("number, result", [
    (2, 1),
    (3, 1),
    (4, 5),
    (90, 100),
    (7, 5),
    (9, 10),
    (400, 500),
    (8, 5),
])
def test_find_closest_number_that_has_its_own_char(number, result):
    assert _find_closest_number_that_has_its_own_character(number) == result


@pytest.mark.parametrize("number, result", [
    (1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), (8, "VIII"), (9, "IX"),
    (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"),
    (400, "CD"), (500, "D"), (900, "CM"), (1000, "M"), (1994, "MCMXCIV"),
    (58, "LVIII"), (20, "XX"), (34, "XXXIV"), (49, "XLIX")
])
def test_converts_number_to_roman_numeral(number, result):

    assert integer_to_roman(number) == result
