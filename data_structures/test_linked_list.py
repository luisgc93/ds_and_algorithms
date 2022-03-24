from data_structures.linked_list import LinkedList


def test_linked_list():
    l1 = LinkedList(nodes=[1, 2, 3])

    assert l1.__repr__() == "1 -> 2 -> 3"
    assert [item.data for item in l1] == [1, 2, 3]
