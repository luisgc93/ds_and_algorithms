import pytest

from primitive_types.primitive_types import compute_parity


@pytest.mark.parametrize("number, expected_parity", [
    (1, 1), (2, 0), (3, 1), (4, 1), (5, 0), (6, 1),
    (7, 0), (8, 0), (9, 1), (10, 0), (11, 1), (136, 0)
])
def test_returns_parity(number, expected_parity):
    assert compute_parity(number) == expected_parity
