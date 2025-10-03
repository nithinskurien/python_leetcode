# 16. 3Sum Closest
#
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
# Constraints:
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
#
# Logic:
# We can sort the numbers, then we fix one number and then move the left and right so that the sum is closer to the
# target. We then calculate the distance of the sum and the target and override the result to the lower value.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[index] + nums[left] + nums[right]
                if currSum == target:
                    return target
                if abs(currSum - target) < abs(res - target):
                    res = currSum
                if currSum < target:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    print(Solution().threeSumClosest([0, 0, 0], 0))
