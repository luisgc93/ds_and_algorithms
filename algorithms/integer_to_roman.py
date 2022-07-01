"""
Given an integer, convert it to a roman numeral.
For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27
is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is
written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There
are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""
from typing import Tuple, List

NUMBERS_THAT_HAVE_ITS_OWN_CHAR = [1, 5, 50, 100, 500, 1000]


def _split_into_powers_of_10(number: int) -> List[Tuple]:
    multiplier_factor = 10
    results = []
    number = str(number)
    number_list = [n for n in number]
    number_list.reverse()  # we want to process smallest number first e.g. 65 -> 5, 6
    for i, n in enumerate(number_list):
        results.append((int(n), multiplier_factor**i))

    results.reverse()
    return results


def _find_closest_number_that_has_its_own_character(number: int) -> int:
    deltas = [abs(n - number) for n in NUMBERS_THAT_HAVE_ITS_OWN_CHAR]
    lowest_diff = min(deltas)
    index = deltas.index(lowest_diff)
    return NUMBERS_THAT_HAVE_ITS_OWN_CHAR[index]


def integer_to_roman(number: int) -> str:
    # roman numerals are written in the order that they're read (largest to smallest)
    # steps:
    # 1. if number has its own character (stored in dict) -> return number
    # 2. else, split the number into powers of 10 e.g. 965 = [(9, 100), (6, 10), (5, 1)]
    # 3. if number has its own character (stored in dict) -> return number and add to list
    # 4. else, for each number part, find the closest of numbers that has its own character
    # e.g. 60 -> 50
    # 5. if number is 4 or 9 -> get closest and use subtraction method e.g. 90 = XC
    # 6. else -> get closest and use addition method e.g. 60 = LX

    # 1st item in tuple is the character for the number, the 2nd one the is the character
    # that gets added or subtracted
    result = []
    roman_dict = {
        1: ("I", "I", 1),
        5: ("V", "I", 1),
        10: ("X", "I", 1),
        50: ("L", "X", 10),
        100: ("C", "X", 10),
        500: ("D", "C", 100),
        1000: ("M", "C", 100)
    }

    number_has_its_own_char = roman_dict.get(number) is not None
    # 1. if number has its own character (stored in dict) -> return number
    if number_has_its_own_char:
        return roman_dict.get(number)[0]

    # 2. else , split the number into powers of 10
    number_in_powers_of_10 = _split_into_powers_of_10(number)
    for number, multiplier_factor in number_in_powers_of_10:
        if number == 0:
            continue
        number = number * multiplier_factor
        if roman_dict.get(number):
            # 3. if number has its own character (stored in dict) -> return number and add to list
            result.append(roman_dict.get(number)[0])
        else:
            # 4. else, for each number part, find the closest of numbers that has its own character
            closest_number = _find_closest_number_that_has_its_own_character(number)
            # 5. if number is 4 or 9 -> get closest and use subtraction method e.g. 90 = XC
            if number in [4, 40, 400, 9, 90, 900]:
                number_of_times_we_sub = abs(number - closest_number) // roman_dict.get(closest_number)[2]
                number_in_roman = (roman_dict.get(closest_number)[1] * number_of_times_we_sub) \
                    + roman_dict.get(closest_number)[0]
                result.append(number_in_roman)
            else:
                # 6. else -> get closest and use addition method e.g. 60 = LX
                number_of_times_we_add = number - closest_number
                number_in_roman = roman_dict.get(closest_number)[0] + \
                    (roman_dict.get(closest_number)[1] * number_of_times_we_add)
                result.append(number_in_roman)

    return "".join(result)
