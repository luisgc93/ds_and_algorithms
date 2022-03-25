from typing import List

import pytest

from algorithms.add_two_numbers import ListNode, add_two_numbers


def _convert_node_to_list(node: ListNode) -> List:
    result = []
    if node.next is None:
        return [node.val]

    while node.next is not None:
        result.append(node.val)
        node = node.next
    return result


@pytest.mark.parametrize("l1, l2, expected", [
    (ListNode(val=2, next_item=ListNode(val=4, next_item=ListNode(val=3))),  # l1
     ListNode(val=5, next_item=ListNode(val=6, next_item=ListNode(val=4))),  # l2
     ListNode(val=7, next_item=ListNode(val=0, next_item=ListNode(8)))  # expected
     ),
    (ListNode(val=0),  # l1
     ListNode(val=0),  # l2
     ListNode(val=0)  # expected
     ),
    (ListNode(val=4, next_item=ListNode(val=2, next_item=ListNode(val=1))),  # l1
     ListNode(val=5, next_item=ListNode(val=9)),  # l2
     ListNode(val=9, next_item=ListNode(val=1, next_item=ListNode(2)))  # expected
     ),
])
def test_add_two_numbers(l1, l2, expected):
    result = add_two_numbers(l1, l2)

    assert _convert_node_to_list(result) == _convert_node_to_list(expected)

