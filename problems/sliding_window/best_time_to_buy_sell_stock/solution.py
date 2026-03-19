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

# 7, 1, 5, 3, 6, 4
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

