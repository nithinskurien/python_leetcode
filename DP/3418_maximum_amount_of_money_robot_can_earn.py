# 3418. Maximum Amount of Money Robot Can Earn
#
# You are given an m x n grid. A robot starts in the top-left corner of the grid (0, 0) and wants to reach the
# bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.
#
# The grid contains a value coins[i][j] in each cell:
#
# If coins[i][j] >= 0, the robot gains that many coins. If coins[i][j] < 0, the robot encounters a robber,
# and the robber steals the absolute value of coins[i][j] coins. The robot has a special ability to neutralize
# robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.
#
# Note: The robot's total coins can be negative.
#
# Return the maximum profit the robot can gain on the route.
#
#
#
# Example 1:
#
# Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
#
# Output: 8
#
# Explanation:
#
# An optimal path for maximum coins is:
#
# Start at (0, 0) with 0 coins (total coins = 0). Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1). Move to (
# 1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total
# coins = 1). Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4). Move to (2, 2), gaining 4 coins (total coins
# = 4 + 4 = 8). Example 2:
#
# Input: coins = [[10,10,10],[10,10,10]]
#
# Output: 40
#
# Explanation:
#
# An optimal path for maximum coins is:
#
# Start at (0, 0) with 10 coins (total coins = 10).
# Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
# Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
# Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).
#
#
# Constraints:
#
# m == coins.length
# n == coins[i].length
# 1 <= m, n <= 500
# -1000 <= coins[i][j] <= 1000
#
# Logic:
# 🧠 Short explanation
#
# This is a dynamic programming (DP) grid path algorithm with a twist.
#
# 🚶‍♂️ What it's doing
#
# You move from top-left → bottom-right in a grid (coins), only going:
#
# down or right
#
# Each cell has a value (positive or negative), and you want to maximize the total sum.
#
# ⚡ Special rule
#
# You are allowed to skip up to 2 negative cells (i.e., not add their value).
#
# 📦 DP definition
# dp[i][j][k]
#
# = maximum sum you can get reaching cell (i, j)
# using at most k skips of negative values
#
# k = 0, 1, 2
# 🔁 Transition
#
# From top or left:
#
# Take the cell value
#
# curr + dp[prev][k]
#
# If current is negative and you still have skips → skip it
#
# dp[prev][k - 1]
#
# Take the maximum of all choices.
#
# 🏁 Base case
#
# Start at (0,0):
#
# If negative and you can skip → start with 0
# Otherwise → take its value
# 🎯 Final answer
# dp[m-1][n-1][2]
#
# = best sum reaching the end with up to 2 skips available
#
# 🧩 In one sentence
#
# 👉 Find the max path sum in a grid while being allowed to ignore up to 2 negative cells.
#
from cmath import inf


class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    curr = coins[i][j]
                    if i == 0 and j == 0:
                        if curr < 0 < k:
                            dp[i][j][k] = 0
                        else:
                            dp[i][j][k] = curr
                        continue
                    res = -inf
                    if i > 0:
                        res = max(res, curr + dp[i - 1][j][k])
                        if curr < 0 and k:
                            res = max(res, dp[i - 1][j][k - 1])
                    if j > 0:
                        res = max(res, curr + dp[i][j - 1][k])
                        if curr < 0 and k:
                            res = max(res, dp[i][j - 1][k - 1])

                    dp[i][j][k] = res

        return dp[-1][-1][2]