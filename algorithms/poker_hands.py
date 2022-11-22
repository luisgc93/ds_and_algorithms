"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks
tie, for example, both players have a pair of queens, then highest cards in each hand are
compared (see example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the
file contains ten cards (separated by a single space): the first five are Player 1's cards and
the last five are Player 2's cards. You can assume that all hands are valid (no invalid
characters or repeated cards), each player's hand is in no specific order, and in each hand
there is a clear winner.

How many hands does Player 1 win?

"""
from collections import Counter
from typing import List

player_1_wins = 0


CARD_TO_SCORE = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

HAND_TO_SCORE = {
    "high_card": 1,
    "one_pair": 2,
    "two_pairs": 3,
    "three_of_a_kind": 4,
    "straight": 5,
    "flush": 6,
    "full_house": 7,
    "four_of_a_kind": 8,
    "straight_flush": 9,
    "royal_flush": 10,
}


PAIR_POINTS = [
    HAND_TO_SCORE["one_pair"],  # e.g. 2, 2
    HAND_TO_SCORE["two_pairs"],  # e.g. 2, 2, 4, 4
]


THREE_OF_A_KIND_POINTS = [
    HAND_TO_SCORE["three_of_a_kind"],  # e.g. 2, 2, 2
    HAND_TO_SCORE["full_house"],  # e.g. 2, 2, 2, 4, 4
]


FOUR_OF_A_KIND_POINTS = [
    HAND_TO_SCORE["four_of_a_kind"],  # e.g. 2, 2, 2, 2
]


def value_of_highest_card(hand_values: List[str]) -> int:
    highest_card_value = 0
    for card in hand_values:
        score = CARD_TO_SCORE[card]
        if score > highest_card_value:
            highest_card_value = score
    return highest_card_value


def value_of_highest_card_outside_of_pair(hand_values: List[str]) -> int:
    highest_card_in_pair = highest_value_in_pair(hand_values)
    highest_card_value = 0
    for card in hand_values:
        score = CARD_TO_SCORE[card]
        if score > highest_card_value and score != highest_card_in_pair:
            highest_card_value = score
    return highest_card_value


def highest_value_in_pair(values: List[str]) -> int:
    if number_of_pairs(values) == 0:
        raise ValueError("No pair found")
    repeated = (Counter(values) - Counter(set(values))).keys()
    highest = 0
    for card in repeated:
        if CARD_TO_SCORE[card] > highest:
            highest = CARD_TO_SCORE[card]
    return highest


def highest_value_in_three_of_a_kind(values: List[str]) -> int:
    if three_of_a_kind(values) is False:
        raise ValueError("3 of a kind not found")
    value_to_frequency = {}
    for value in values:
        if value in value_to_frequency:
            value_to_frequency[value] += 1
        else:
            value_to_frequency[value] = 1
    return int(max(value_to_frequency, key=value_to_frequency.get))


def highest_value_in_four_of_a_kind(values: List[str]) -> int:
    if four_of_a_kind(values) is False:
        raise ValueError("4 of a kind not found")
    value_to_frequency = {}
    for value in values:
        if value in value_to_frequency:
            value_to_frequency[value] += 1
        else:
            value_to_frequency[value] = 1
    return int(max(value_to_frequency, key=value_to_frequency.get))


def royal_flush(values: List[str], suits: List[str]) -> bool:
    if {"T", "J", "Q", "K", "A"} == set(values):
        if len(set(suits)) == 1:
            return True
    return False


def straight(values: List[str]) -> bool:
    int_values = [CARD_TO_SCORE[value] for value in values]
    sorted_values = sorted(int_values)
    min_value = min(sorted_values)
    max_value = max(sorted_values)
    return [number for number in range(min_value, max_value + 1)] == sorted_values


def flush(suits: List[str]) -> bool:
    return len(set(suits)) == 1


def three_of_a_kind(values: List[str]) -> bool:
    count = Counter(values) - Counter(set(values))
    for i in count:
        if count[i] == 2:
            return True
    return False


def number_of_pairs(values: List[str]) -> int:
    count = Counter(values) - Counter(set(values))
    pairs = 0
    for i in count:
        if count[i] == 1:
            pairs += 1
    return pairs


def full_house(values: List[str]) -> bool:
    return three_of_a_kind(values) and number_of_pairs(values) == 1


def four_of_a_kind(values: List[str]) -> bool:
    dup = Counter(values) - Counter(set(values))
    for i in dup:
        if dup[i] == 3:
            return True
    return False


def straight_flush(values: List[str], suits: List[str]) -> bool:
    return straight(values) and flush(suits)


def evaluate_hand(values: List[str], suits: List[str]) -> int:
    if royal_flush(values, suits):
        return HAND_TO_SCORE["royal_flush"]
    elif straight_flush(values, suits):
        return HAND_TO_SCORE["straight_flush"]
    elif four_of_a_kind(values):
        return HAND_TO_SCORE["four_of_a_kind"]
    elif full_house(values):
        return HAND_TO_SCORE["full_house"]
    elif flush(suits):
        return HAND_TO_SCORE["flush"]
    elif straight(values):
        return HAND_TO_SCORE["straight"]
    elif three_of_a_kind(values):
        return HAND_TO_SCORE["three_of_a_kind"]
    elif number_of_pairs(values) == 2:
        return HAND_TO_SCORE["two_pairs"]
    elif number_of_pairs(values) == 1:
        return HAND_TO_SCORE["one_pair"]
    elif number_of_pairs(values) == 0:
        return HAND_TO_SCORE["high_card"]


def convert_hand_to_suits(hand: List[str]) -> List[str]:
    return [card[-1] for card in hand]


def convert_hand_to_values(hand: List[str]) -> List[str]:
    return [card[:-1] for card in hand]


def pick_winning_hand(
        values_hand_1: List[str], suits_hand_1: List[str], values_hand_2: List[str], suits_hand_2: List[str]
) -> int:
    hand_1_score = evaluate_hand(values_hand_1, suits_hand_1)
    hand_2_score = evaluate_hand(values_hand_2, suits_hand_2)
    if hand_1_score > hand_2_score:
        return 1
    elif hand_2_score > hand_1_score:
        return 2
    else:
        if hand_1_score in PAIR_POINTS:
            if highest_value_in_pair(values_hand_1) > highest_value_in_pair(values_hand_2):
                return 1
            elif highest_value_in_pair(values_hand_2) > highest_value_in_pair(values_hand_1):
                return 2
            # both cards have the same pair and also have the same highest card - look for next highest
            elif value_of_highest_card_outside_of_pair(values_hand_1) > value_of_highest_card_outside_of_pair(values_hand_2):  # noqa
                return 1
            elif value_of_highest_card_outside_of_pair(values_hand_2) > value_of_highest_card_outside_of_pair(values_hand_1):  # noqa
                return 2
        if hand_1_score in THREE_OF_A_KIND_POINTS:
            if highest_value_in_three_of_a_kind(values_hand_1) > highest_value_in_three_of_a_kind(values_hand_2):
                return 1
            elif highest_value_in_three_of_a_kind(values_hand_2) > highest_value_in_three_of_a_kind(values_hand_1):
                return 2
        if hand_1_score in FOUR_OF_A_KIND_POINTS:
            if highest_value_in_four_of_a_kind(values_hand_1) > highest_value_in_four_of_a_kind(values_hand_2):
                return 1
            elif highest_value_in_four_of_a_kind(values_hand_2) > highest_value_in_four_of_a_kind(values_hand_1):
                return 2
        else:
            if value_of_highest_card(values_hand_1) > value_of_highest_card(values_hand_2):
                return 1
            elif value_of_highest_card(values_hand_2) > value_of_highest_card(values_hand_1):
                return 2
            else:
                return 0


if __name__ == "__main__":
    with open("poker.txt") as f:
        hand_lines = f.readlines()
        for games in hand_lines:
            hands = games.split(" ")
            hand_1 = hands[:5]
            hand_2 = hands[5:]
            hand_2[-1] = hand_2[-1].replace("\n", "")

            # split hands into suits and values
            hand_1_suits = convert_hand_to_suits(hand_1)
            hand_1_values = convert_hand_to_values(hand_1)

            hand_2_suits = convert_hand_to_suits(hand_2)
            hand_2_values = convert_hand_to_values(hand_2)

            result = pick_winning_hand(hand_1_values, hand_1_suits, hand_2_values, hand_2_suits)

            if result == 1:
                player_1_wins += 1
    print(player_1_wins)
