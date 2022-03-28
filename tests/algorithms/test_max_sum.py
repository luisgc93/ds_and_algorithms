import pytest

from algorithms.max_sum import calculate_max_sum


@pytest.mark.parametrize("arr, k, expected_result", [
    #([100, 200, 300, 400], 2, 700),
    #([100], 1, 100),
    ([200, 50, 600, 0], 2, 650),

])
def test_calculate_max_sum(arr, k, expected_result):
    assert calculate_max_sum(arr, k) == expected_result
