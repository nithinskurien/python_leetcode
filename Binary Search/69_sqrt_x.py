# 69. Sqrt(x)
#
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned
# integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
# Example 1:
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
#
#
# Constraints:
#
# 0 <= x <= 231 - 1
#
# Logic:
# Given the constraints we can use binary search to find the number that when squared is less than or equal to x

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
                res = mid
            else:
                return mid
        return res