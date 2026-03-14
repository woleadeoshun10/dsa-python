"""
Problem: Best Time to Buy and Sell Stock
Pattern: Array / Min Tracking
Difficulty: Easy

Time Complexity: O(n)
We scan the array once.

Space Complexity: O(1)
Only constant variables are used.
"""


class Solution:
    def maxProfit(self, prices):

        minPrice = price[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)

        return maxProfit


