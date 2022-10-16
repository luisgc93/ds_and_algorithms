"""
Change exactly one character in the string to another ASCII character so that the string
meets the following conditions:
1. The new string is lower alphabetically than the new string
2. The new string is the lowest value string alphabetically that can be created from the
original palindrome after making only one change
3. The new string is not a palindrome

Return the new string of if it not possible to create a string that meets the criteria,
return the string IMPOSSIBLE

Example: palindrome_str = "aaabbaaa"
- possible strings lower alphabetically after one change are ["aaaabaaa", "aaabaaaa"]
- "aaaabaaa" is not a palindrome and is the lowest string that can be created from
 palindrome_str

"""


def _is_palindrome(string: str) -> bool:
    return string == string[::-1]


def break_palindrome(palindrome: str) -> str:
    result = ""
    changes = 0
    for letter in palindrome:
        if letter == "a":
            result += letter
        else:
            if changes == 0:
                result += "a"
                changes += 1
            else:
                result += letter
    if _is_palindrome(result):
        return "IMPOSSIBLE"
    return result
