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
    This approach involves storing every single substring that does not contain duplicated letters.
    Results in Time Limit Exceeded error for very large strings but works with small inputs.
    """
    if len(string) == 1:
        return 1
    substrings = []
    while len(string) > 1:
        for i in range(1, len(string) + 1):
            if len(string[:i]) == len(set(string[:i])):
                substrings.append(string[:i])
        string = string[1:]

    substrings.sort(key=len)
    return len(substrings[-1]) if substrings else 0


def length_of_longest_substring_optimized(string: str) -> int:
    ans = 0  # keep track of longest substring len seen so far
    sub = ''
    for char in string:
        if char not in sub:
            sub += char
            ans = max(ans, len(sub))
        else:
            cut_index = sub.index(char)
            sub = sub[cut_index + 1:] + char
    return ans
