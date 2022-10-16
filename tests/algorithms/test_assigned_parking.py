import pytest

from algorithms.assigned_parking import min_fuel


@pytest.mark.parametrize("x, y, result", [
    ([1, 4], [1, 4], 5),
    ([1, 5], [1, 5], 7),
    ([4, 6, 4, -4, 1], [-1, 1, -5, -4, 5], 23),
])
def test_min_fuel(x, y, result):
    assert min_fuel(x, y) == result
