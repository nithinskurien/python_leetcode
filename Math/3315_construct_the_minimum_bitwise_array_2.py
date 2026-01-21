# 3314. Construct the Minimum Bitwise Array I
#
# You are given an array nums consisting of n prime integers.
#
# You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] +
# 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
#
# Additionally, you must minimize each value of ans[i] in the resulting array.
#
# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
#
#
#
# Example 1:
#
# Input: nums = [2,3,5,7]
#
# Output: [-1,1,4,3]
#
# Explanation:
#
# For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2, so ans[0] = -1.
# For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1, because 1 OR (1 + 1) = 3.
# For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4, because 4 OR (4 + 1) = 5.
# For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3, because 3 OR (3 + 1) = 7.
# Example 2:
#
# Input: nums = [11,13,31]
#
# Output: [9,12,15]
#
# Explanation:
#
# For i = 0, the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9, because 9 OR (9 + 1) = 11.
# For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12, because 12 OR (12 + 1) = 13.
# For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15, because 15 OR (15 + 1) = 31.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 2 <= nums[i] <= 109
# nums[i] is a prime number.
#
# Logic:
# when you add 1 to a number, it flips a trailing sequence
# of 1-bits to 0s and sets the next 0-bit to 1. For example:
#
# 5 (binary 101) + 1 = 6 (binary 110)
# When you OR these: 101 | 110 = 111 (which is 7)
#
# The algorithm:
#
# Start with d = 1 (a bitmask with just the rightmost bit set)
# While the current bit is 1 in nums[i]:
#
# Try res = nums[i] - d as a candidate answer
# Shift d left by 1 (d <<= 1) to check the next bit
#
#
# Why this works: The loop finds the rightmost 0-bit in nums[i]. The answer is nums[i] minus the value of the
# rightmost 1-bit position, which removes that bit.

class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums
