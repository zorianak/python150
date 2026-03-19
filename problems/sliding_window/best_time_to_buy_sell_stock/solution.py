from typing import List, Optional

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day. Return the maximum profit you can achieve from this transaction.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Day 1: day we buy the stonks, left hand of the window
            Day 2: day we sell the stonks, right hand of hte window
            maxProfit: d2 - d1
        """

        l, r = 0, 1
        maxP = 0 

        while r < len(prices):
            # check if its a profit
            if prices[l] < prices[r]:
                result = prices[r] - prices[l]
                maxP = max(maxP, result)
            else:
                l = r
            r += 1
        return maxP
