from typing import List, Optional

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash - contain a key for each number in the array, value as frequency
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            frequency[cnt].append(num)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

        pass
