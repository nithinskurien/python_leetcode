# Q3. Max Consecutive Ones
#
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1,1,1] Output: 3 Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3. Example 2:
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
#
# Logic:
# We can increment a temp variable every time we iterate the array and reset the variable when we see a '0'. At every
# iteration we check if this new length is larger than the previous one and replace it if yes. Return the result at the
# end of all the iterations.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = 0
        curr = 0
        for num in nums:
            curr += 1
            if num == 0:
                curr = 0
            res = max(res, curr)
        return res