# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#
# Logic:
# Sorting the input list to simplify finding triplets and avoiding duplicates. Iterating through each number as
# the first element of a triplet. Using two pointers (left and right) to find two other numbers that sum to the
# negative of the first number (so the total is zero). Adjusting pointers based on whether the sum is too small (move
# left right) or too large (move right left). When a triplet summing to zero is found, adding it to the result and
# skipping duplicates. Skipping duplicate first numbers to ensure unique triplets. Returning the list of all valid
# triplets.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for index in range(len(nums)):
            if index != 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res