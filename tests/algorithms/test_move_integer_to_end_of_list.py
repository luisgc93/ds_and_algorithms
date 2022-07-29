from algorithms.move_integer_to_end_of_list import move_to_end


def test_moves_item_to_end_of_list():
    assert move_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)[4:] == [2, 2, 2, 2]
