# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
# approach, which is more subtle.
#
# Logic:
# We need to get the maximum sum so having negative sum is not favourable, so we could reset sum to zero when we do so.
# We can iterate the array and add the element to a curr sum, and then compare if the curr sum is greater than max sum
# when the currSum becomes less than 0 we reset currSum and continue
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            currSum = max(currSum, 0)
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum
