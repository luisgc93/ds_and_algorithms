import pytest

from algorithms.add_two_numbers import add_two_numbers, ListNode


@pytest.mark.parametrize("l1, l2, expected", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
])
def test_add_two_numbers(l1, l2, expected):

    assert add_two_numbers(ListNode(l1), ListNode(l2)) == ListNode(expected)
