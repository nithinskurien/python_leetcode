#
#
# You are given an integer array coins representing coins of different denominations and an integer amount
# representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up
# by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Constraints:
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
#
# Logic:
# We split the problem in smaller sub problems and use memoization to iterate over the least possible amounts and the
# coins needed to make that amount possible, then we iterate over the amount to work our way up.


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], 1 + dp[x - coin])
        return dp[-1] if dp[-1] != float('inf') else -1


class SolutionRecursive:
    def minCoinNeeded(self, amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]
        minCoins = float('inf')
        for coin in self.coins:
            if coin <= amount:
                coinNeeded = self.minCoinNeeded(amount - coin)
                minCoins = min(minCoins, coinNeeded)
        if minCoins != float('inf'):
            minCoins += 1
        self.memo[amount] = minCoins
        return minCoins

    def coinChange(self, coins: list[int], amount: int) -> int:
        self.memo = {}
        self.memo[0] = 0
        self.coins = sorted(coins)
        for coin in self.coins:
            if coin <= amount:
                self.memo[coin] = 1
        answer = self.minCoinNeeded(amount)
        return answer if answer != float('inf') else -1