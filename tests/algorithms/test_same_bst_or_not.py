from algorithms.same_bst_or_not import is_same_bst


def test_same_bst():
    assert is_same_bst([2, 4, 3, 1], [2, 1, 4, 3]) is True
    assert is_same_bst(
        [10, 15, 8, 12, 94, 81, 5, 2, 11],
        [10, 8, 5, 15, 2, 12, 11, 94, 81]
    ) is True

