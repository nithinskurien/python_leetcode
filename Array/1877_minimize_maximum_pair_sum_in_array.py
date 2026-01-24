# 1877. Minimize Maximum Pair Sum in Array
#
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
#
# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5,
# 8) = 8. Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
#
# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.
#
#
#
# Example 1:
#
# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
# Example 2:
#
# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 105
# n is even.
# 1 <= nums[i] <= 105
#
# Logic:
# To make sure we are adding the pairs so that they are minimum we can sort the array and add the first with the last
# and so on. We can then in one iteration after sorting check which pair has the largest sum.

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for index in range(n // 2):
            temp = nums[index] + nums[(n - 1) - index]
            res = max(res, temp)
        return res