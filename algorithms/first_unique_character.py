"""
Return the 1-based index of the first character that has a
single occurrence in a string
"""


def get_unique_character(input_string: str) -> int:
    # TODO: improve performance
    for index, letter in enumerate(input_string):
        if input_string.count(letter) > 1:
            continue
        else:
            return index + 1
    return -1
