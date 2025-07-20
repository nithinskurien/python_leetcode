class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        buy = [0]*len(prices)
        sell = [0]*len(prices)
        buy[0] = -prices[0]
        for index in range(1, len(prices)):
            sell[index] = max(sell[index - 1], buy[index - 1] + prices[index] - fee)
            buy[index] = max(buy[index - 1], sell[index - 1] - prices[index])
        return sell[len(prices) - 1]