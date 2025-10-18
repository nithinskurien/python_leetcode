# 3397. Maximum Number of Distinct Elements After Operations
#
# You are given an integer array nums and an integer k.
#
# You are allowed to perform the following operation on each element of the array at most once:
#
# Add an integer in the range [-k, k] to the element.
# Return the maximum possible number of distinct elements in nums after performing the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,3,3,4], k = 2
#
# Output: 6
#
# Explanation:
#
# nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.
#
# Example 2:
#
# Input: nums = [4,4,4,4], k = 1
#
# Output: 3
#
# Explanation:
#
# By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 109
#
# Logic:
# We can use a greedy approach to make the smallest elements of the array the smallest possible by doing operations on
# them allowing more room for the later nums to fit better. Every time we set the num to be the lowest (max of the
# num - k or prev low_bound + 1) if the element is equal or less than the num + k we can increase the count and update
# the low bound


class Solution:

    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 0
        low_bound = float('-inf')
        for num in nums:
            curr = max(num - k, low_bound + 1)
            if curr <= num + k:
                res += 1
                low_bound = curr
        return res
