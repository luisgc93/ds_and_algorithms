"""
You are given an array of integers and an integer. Write a function that moves all
instances of that integer in the array to the end of the array and returns the array

The function doesn't need to maintain the order of the other integers

Sample input:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
Sample output: [1, 3, 4, 2, 2, 2, 2, 2] (the numbers 1, 3, and 4 could be ordered differently)
"""
from typing import List


def move_to_end(list_of_ints: List[int], to_move):
    list_of_target_number = []
    other_numbers = []
    for item in list_of_ints:
        if item == to_move:
            list_of_target_number.append(item)
        else:
            other_numbers.append(item)
    breakpoint()
    return other_numbers + list_of_target_number



