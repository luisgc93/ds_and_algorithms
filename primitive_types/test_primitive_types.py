import pytest

from primitive_types.primitive_types import compute_parity, count_bits_that_are_set_to_one, parity, \
    parity_improved_version, parity_improved_version_2


@pytest.mark.parametrize("number, expected_parity", [
    (0, 0), (1, 1), (2, 1), (3, 0), (4, 1), (5, 0), (6, 0),
    (7, 1), (8, 1), (9, 0), (10, 0), (11, 1), (136, 0)
])
def test_returns_parity(number, expected_parity):
    assert parity(number) == expected_parity
    assert compute_parity(number) == expected_parity
    assert parity_improved_version(number) == expected_parity
    assert parity_improved_version_2(number) == expected_parity


@pytest.mark.parametrize("number, expected_number", [
    (1, 1), (2, 1), (3, 2), (4, 1), (5, 2), (6, 2),
    (7, 3), (8, 1), (9, 2), (10, 2), (11, 3)
])
def test_number_of_bits_set_to_one(number, expected_number):
    assert count_bits_that_are_set_to_one(number) == expected_number
