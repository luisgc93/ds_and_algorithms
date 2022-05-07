"""
Return the 1-based index of the first character that has a single occurrence in a string
"""


def get_unique_character(input_string: str) -> int:
    for index, character in enumerate(input_string):
        if input_string.count(character) > 1:
            continue
        else:
            return index + 1
    return -1


def get_unique_character_improved_performance(input_string: str) -> int:
    """
    Here we use a dictionary for better performance
    https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38
    """
    frequency = {}
    for character in input_string:
        if character not in frequency:
            frequency[character] = 1
        else:
            frequency[character] += 1
    for i in range(len(input_string)):
        if frequency[input_string[i]] == 1:
            return i + 1
    return -1
