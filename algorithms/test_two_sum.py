import pytest

from algorithms.two_sum import two_sum, two_sum_suggested, two_sum_improved


@pytest.mark.parametrize("nums, target, expected_answer", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, 7, 11, 15], 13, [0, 2]),
    ([-3, 2, 0, 1], -3, [0, 2]),
    ([-3, 2, 0, 1, 5, 18, 11, 932], 20, [1, 5]),
    ([1, 1, 2, 0], 2, [0, 1]),
    ([2, 5, 5, 11], 10, [1, 2]),
    ([3, 4, 9, 6, 4], 8, [1, 4]),
])
def test_two_sum(nums, target, expected_answer):
    assert two_sum(nums, target) == expected_answer
    assert two_sum_suggested(nums, target) == expected_answer
    assert two_sum_improved(nums, target) == expected_answer
