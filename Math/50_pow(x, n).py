# 50. Pow(x, n)
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#
#
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#
# Constraints:
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104
#
# Logic:
# The function computes x^n using fast exponentiation (divide and conquer) instead of multiplying x repeatedly.
#
# It works by recursively breaking the problem into smaller parts:
#
# To compute x^n, it first computes x^(n//2)
# Then:
# If n is even:
# x^n = (x^(n//2)) * (x^(n//2))
# If n is odd:
# x^n = x * (x^(n//2)) * (x^(n//2))
#
# This reduces the number of operations significantly.
#
# Base cases:
#
# If n == 0, return 1
# If x == 0, return 0
#
# For negative powers:
#
# First compute x^(abs(n))
# If n is negative:
# x^(-n) = 1 / (x^n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            temp = helper(x, n // 2)
            return x * temp * temp if n % 2 != 0 else temp * temp

        ans = helper(x, abs(n))
        return ans if n > 0 else 1 / ans
