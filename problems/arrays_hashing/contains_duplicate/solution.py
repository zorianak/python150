from typing import List, Optional

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
