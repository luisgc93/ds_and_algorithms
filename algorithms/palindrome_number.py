"""
LEETCODE QUESTION
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(number: int) -> bool:
    """
    Leetcode submission results:
    Runtime: 83 ms, faster than 60.68% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14 MB, less than 21.21% of Python3 online submissions for Palindrome Number.
    """
    if number < 0:
        return False

    string_number = str(number)
    reversed_string_number = string_number[::-1]

    return int(reversed_string_number) == number


def is_palindrome_without_string_conversion(number: int) -> bool:
    """
    Leetcode submission results:
    Runtime: 90 ms, faster than 51.57% of Python3 online submissions for Palindrome Number.
    Memory Usage: 13.9 MB, less than 65.27% of Python3 online submissions for Palindrome Number.
    """
    # palindromes can't be negative or multiples of 10 (other than 0)
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    # all single-digit numbers are palindromes
    if int(number/10) == 0:
        return True

    original_number = number
    reversed_number = 0
    while number > 1:
        # int(number) % 10 returns the number's last digit
        reversed_number = reversed_number * 10 + (int(number) % 10)
        number = number / 10
    return reversed_number == original_number
