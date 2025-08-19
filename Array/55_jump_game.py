# 55. Jump Game
#
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4] Output: false Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
#
# Logic:
# We will set the goal to reach as the final position, we will then iterate over the array backwards and see if there is
# an index from where the final position is reachable if it is then we set the final position to be the new goal. Then
# we continue till we reach the start of the array. In the end we will check if the final position is the start as if
# the goal is start that means we have some way to reach the end from the start.


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        finalPosition = len(nums) - 1
        for index in range(finalPosition, -1, -1):
            if (index + nums[index]) >= finalPosition:
                finalPosition = index
        return finalPosition == 0
