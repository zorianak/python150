from collections import defaultdict
import string
from typing import List, Optional

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # want a dictionary with default values
        res = defaultdict(list)
        for str in strs:
            # array that contains each alphabet char can be incremented
            count = [0] * 26
            for c in str:
                # increment as its found
                count[ord(c) - ord('a')] += 1
            # result should then be teh list of strings
            res[tuple(count)].append(str)
        return list(res.values())
