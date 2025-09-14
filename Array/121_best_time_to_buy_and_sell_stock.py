# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
#
# Logic:
# We can initialise the max profit to be zero and the buy price to be the first value in the array. As we progress to
# the next value in the array we can check if the price is lower than our buy signal if it is then we will assign our
# new buy signal to be that price, else we can check the profit and substitute the max profit if the profit is larger
# we can return the max profit in the end.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            else:
                maxProfit = max(maxProfit, price - buy)
        return maxProfit
