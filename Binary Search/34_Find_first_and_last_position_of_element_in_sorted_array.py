# 34. Find First and Last Position of Element in Sorted Array
#
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109
#
# Logic:
# We can use binary search and find the leftmost & rightmost limit of the target. We can modify the binary search such
# that we will move either left or right till we exhaust all the positions of the target. We can then use binary search
# twice, once for finding the leftmost and then the rightmost limit.

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binarySearch(nums: list[int], target: int, leftBias: bool) -> list[int]:
            index, left, right = -1, 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    index = mid
                    if leftBias:
                        right = index - 1
                    else:
                        left = index + 1
            return index

        leftLimit = binarySearch(nums, target, True)
        rightLimit = binarySearch(nums, target, False)
        return [leftLimit, rightLimit]