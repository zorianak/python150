from typing import List, Optional

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # one pointer at the start
        # one at the end
        # compare the two, if ever not equal, return false
        # when they meet, return true
        left, right = 0, len(s) - 1
        while left < right:
            # move if not alphabet/number
            while s[left].isalnum() == False and left < right:
                left += 1
            while s[right].isalnum() == False and left < right:
                right -= 1
            # compare them two, false if not equal
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        pass
