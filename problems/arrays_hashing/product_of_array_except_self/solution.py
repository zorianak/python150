from typing import List, Optional

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # n = len(nums)
        
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         else:
        #             product = nums[j] * product
        #     result.append(product)
        # return result

        # with division
        # prod, zeroes = 1, 0
        # for i in nums:
        #     if i:
        #         prod *= i
        #     else:
        #         zeroes += 1
        # if zeroes > 1: return [0] * len(nums)
        
        # res = [0] * len(nums)
        # for k, c in enumerate(nums):
        #     if zeroes: res[k] = 0 if c else prod
        #     else: res[k] = prod // c
        # return res

        # o(n) without division

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n
        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res
