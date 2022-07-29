"""
An array of integer is said to represent the Binary Search Tree (BST) obtained by
inserting each integer into the array, from left to right, into the BST.

Write a function that takes in two arrays of integers and determines whether these arrays
represent the same BST or not. Note that you're not allowed to construct any BST's in
your code.

A BST is a Binary Tree that consists of only BST nodes. A node is said to be a valid BST
node if and only if it satisfies the BST property: its value is strictly greater than
the values of every node to its left; its value is less than or equal to every value on
its right; and its children nodes are either valid BST nodes themselves or None/Null

Sample Input:
array_one: [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two: [10, 8, 5, 15, 2, 12, 11, 94, 81]

Sample Output:
True
"""
from typing import List


def is_same_bst(array_one: List[int], array_two: List[int]) -> bool:
    # WIP
    return False
