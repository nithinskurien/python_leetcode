# 70. Climbing Stairs
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45
#
# Logic:
# We can break the problem into multiple sub problems where once we compute how many ways we can reach a certain step
# we can use that result to compute the ways to reach larger steps. As we can move only 1 or 2 steps and to reach no
# step or a single step we just have one way of doing so we can use this to compute the later stairs by combining the
# result of the n - 1 and n - 2

class Solution:
    def dp(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n >= 2:
            ways = self.dp(n - 1) + self.dp(n - 2)
            self.memo[n] = ways
            return ways

    def climbStairs(self, n: int) -> int:
        self.memo = {}
        self.memo[0] = 1
        self.memo[1] = 1
        return self.dp(n)