"""
LEETCODE QUESTION
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:  # This is n^2
    index_1 = 0
    index_2 = 1
    while index_1 < len(nums):
        while index_2 < len(nums):
            if nums[index_1] + nums[index_2] == target:
                return [index_1, index_2]
            index_2 += 1
        index_1 += 1
        index_2 = index_1 + 1


# TODO: use hash map or sorting algorithm to reduce time complexity
