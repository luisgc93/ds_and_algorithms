import pytest

from data_structures.linked_list import LinkedList, Node


def test_returns_representation():
    l1 = LinkedList(nodes=[1, 2, 3])

    assert l1.__repr__() == "1 -> 2 -> 3"
    assert [item.data for item in l1] == [1, 2, 3]


def test_iterates_through_list_elements():
    l1 = LinkedList(nodes=[1, 2, 3])

    assert [item.data for item in l1] == [1, 2, 3]


def test_adds_new_node_at_the_beginning():
    l1 = LinkedList(nodes=[1, 2, 3])
    l1.add_first(new_node=Node(0))

    assert l1.__repr__() == "0 -> 1 -> 2 -> 3"


def test_adds_new_node_at_the_end():
    l1 = LinkedList(nodes=[1, 2, 3])
    l1.add_last(new_node=Node(4))

    assert l1.__repr__() == "1 -> 2 -> 3 -> 4"


def test_adds_new_node_after_a_given_item():
    l1 = LinkedList(nodes=[7, 33, 19, 4, 0, 11])
    l1.add_after(target_node_data=4, new_node=Node(4))

    assert l1.__repr__() == "7 -> 33 -> 19 -> 4 -> 4 -> 0 -> 11"


def test_raises_when_adding_a_node_after_an_item_when_list_is_empty():
    l1 = LinkedList(nodes=[])

    with pytest.raises(Exception):
        l1.add_after(target_node_data=4, new_node=Node(4))


def test_raises_when_adding_a_node_after_an_item_when_item_is_not_present_in_list():
    l1 = LinkedList(nodes=[1, 2, 3])

    with pytest.raises(Exception):
        l1.add_after(target_node_data=4, new_node=Node(4))

