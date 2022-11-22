import pytest

from algorithms.poker_hands import evaluate_hand, convert_hand_to_values, convert_hand_to_suits, pick_winning_hand


@pytest.mark.parametrize("hand, score", [
    (["5H", "5C", "6S", "7S", "KD"], 2),
    (["2C", "3S", "8S", "8D", "TD"], 2),
    (["5D", "8C", "9S", "JS", "AC"], 1),
    (["2C", "5C", "7D", "8S", "QH"], 1),
    (["2D", "9C", "AS", "AH", "AC"], 4),
    (["3D", "6D", "7D", "TD", "QD"], 6),
    (["4D", "6S", "9H", "QH", "QC"], 2),
    (["3D", "6D", "7H", "QD", "QS"], 2),
    (["2H", "2D", "4C", "4D", "4S"], 7),
    (["3C", "3D", "3S", "9S", "9D"], 7),
    (["3C", "4C", "5C", "6C", "9D"], 1),
    (["3C", "4C", "5C", "6C", "7C"], 9),
    (["TS", "JS", "QS", "KS", "AS"], 10),
    (["6H", "4H", "5C", "3H", "2H"], 5),
])
def test_evaluates_hand(hand, score):
    values = convert_hand_to_values(hand)
    suits = convert_hand_to_suits(hand)

    assert evaluate_hand(values, suits) == score


@pytest.mark.parametrize("player_1, player_2, expected_winner", [
    (["5H", "5C", "6S", "7S", "KD"], ["2C", "3S", "8S", "8D", "TD"], 2),
    (["5D", "8C", "9S", "JS", "AC"], ["2C", "5C", "7D", "8S", "QH"], 1),
    (["2D", "9C", "AS", "AH", "AC"], ["3D", "6D", "7D", "TD", "QD"], 2),
    (["4D", "6S", "9H", "QH", "QC"], ["3D", "6D", "7H", "QD", "QS"], 1),
    (["2H", "2D", "4C", "4D", "4S"], ["3C", "3D", "3S", "9S", "9D"], 1),
    (["6H", "4H", "5C", "3H", "2H"], ["3S", "QH", "5S", "6S", "AS"], 1),
])
def test_picks_correct_winner(player_1, player_2, expected_winner):
    values_player_1 = convert_hand_to_values(player_1)
    suits_player_1 = convert_hand_to_suits(player_1)

    values_player_2 = convert_hand_to_values(player_2)
    suits_player_2 = convert_hand_to_suits(player_2)

    assert pick_winning_hand(values_player_1, suits_player_1, values_player_2, suits_player_2) == expected_winner
