# 1390. Four Divisors
#
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four
# divisors. If there is no such integer in the array, return 0.
#
#
#
# Example 1:
#
# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:
#
# Input: nums = [21,21]
# Output: 64
# Example 3:
#
# Input: nums = [1,2,3,4,5]
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105
#
# Logic: To find the divisors we do not need to loop all the numbers from 1 till the number, but only till the sqrt
# of the number, as the divisors come in pairs, we can find the second divisor by finding the result of the division
# operation when the remainder is zero. So we can use this information to solve this problem.

from math import floor, sqrt


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            div = set()
            for n in range(1, floor(sqrt(num)) + 1):
                if num % n == 0:
                    div.add(num // n)
                    div.add(n)
                    if len(div) > 4:
                        break
            if len(div) == 4:
                res += sum(div)
        return res