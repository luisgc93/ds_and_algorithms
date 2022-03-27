"""
** Hackerrank question **
The following operations on a string are defined:
- Left shift: A single circular rotation on a string in which the first character
  becomes the last character and all the other characters are shifted one index
  to the left. For example, abcde becomes bcdea after one left shift and cdeab
  after two left shifts.
- Right shift: A single circular rotation on a string in which the last character
  becomes the first character and all the other characters are shifted one index
  to the right. For example, abcde becomes eabcd after one right shift and deabc
  after two right shifts.

"""


def get_shifted_string_original_version(string: str, left_shifts: int, right_shifts: int) -> str:
    for _ in range(left_shifts):
        string = string[1:] + string[0]
    for _ in range(right_shifts):
        string = string[-1] + string[:-1]

    return string


def get_shifted_string_improved(string: str, left_shifts: int, right_shifts: int) -> str:
    if left_shifts == right_shifts:
        return string
    if left_shifts > right_shifts:
        left_shifts = left_shifts - right_shifts
        right_shifts = 0
    elif right_shifts > left_shifts:
        right_shifts = right_shifts - left_shifts
        left_shifts = 0

    if left_shifts == len(string) or right_shifts == len(string):
        return string

    if left_shifts and left_shifts % len(string) == 0 or right_shifts and right_shifts % len(string) == 0:
        return string

    if left_shifts != 0:
        string = string[left_shifts:] + string[:left_shifts]
    if right_shifts != 0:
        string = string[-right_shifts:] + string[:-right_shifts]

    return string


def get_shifted_string_best_version(string: str, left_shifts: int, right_shifts: int) -> str:
    string_length = len(string)
    left_shifts = left_shifts % string_length
    right_shifts = right_shifts % string_length

    left_shift_result = string[left_shifts:] + string[:left_shifts]

    right_shift_result = left_shift_result[-right_shifts:] + left_shift_result[:-right_shifts]

    return right_shift_result
