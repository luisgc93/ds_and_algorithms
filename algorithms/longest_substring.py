"""
LEETCODE QUESTION
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring_brute_force(string: str) -> int:
    """
    This approach involves finding every single substring and then checking whether it contains
    duplicated letters or not. Results in Memory Limit Exceeded error for very large strings but
    works with small inputs.
    """
    if len(string) == 1:
        return 1
    substrings = []
    while len(string) > 1:
        for i in range(1, len(string) + 1):
            substrings.append(string[:i])
        string = string[1:]

    substrings_without_duplicates = [
        substring for substring in substrings
        if len(substring) == len(set(substring))
    ]

    substrings_without_duplicates.sort(key=len)
    return len(substrings_without_duplicates[-1]) if substrings_without_duplicates else 0
