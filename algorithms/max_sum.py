"""
Taken from: https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b

Given an array of integers of size n.
Our aim is to calculate the maximum sum possible for k consecutive elements in the array.

Example:
Input  : arr[] = [100, 200, 300, 400], k = 2
Output : 700
"""
from typing import List


# TODO: FINISH THIS
def calculate_max_sum(arr: List[int], k: int) -> int:
    counter = 0
    max_sum = 0
    current_sum = 0
    for num in arr:
        if counter < k:
            current_sum += num
            counter += 1
        else:
            breakpoint()
            counter = 0
            max_sum = max(max_sum, current_sum + num)
            current_sum = num

    return max(max_sum, current_sum)
