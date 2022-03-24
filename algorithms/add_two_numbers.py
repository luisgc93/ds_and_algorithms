"""
LEETCODE QUESTION
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Reminder: https://realpython.com/linked-lists-python/
Summary - linked lists have better performance for inserting at a non-last position since
you don't have to shift the entire sequence unlike in a regular list.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_item=None):
        self.val = val
        self.next = next_item


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    number_1 = 0
    number_2 = 0
    for digit in l1.val:
        number_1 += digit
    breakpoint()
