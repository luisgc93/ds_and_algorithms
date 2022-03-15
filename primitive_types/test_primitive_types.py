import pytest

from primitive_types.primitive_types import compute_parity


@pytest.mark.parametrize("number, expected_parity", [
    (11, 1),
    (136, 0)
])
def test_returns_parity(number, expected_parity):
    assert compute_parity(number) == expected_parity
