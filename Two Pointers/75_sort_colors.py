# 75. Sort Colors
#
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
# color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
#
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?
#
# Logic:
# We can use 3 pointers low, mid, high. Low and mid, start at zero while the high starts at end. We can iterate the list
# till the mid is less than equal to high. When the mid-value is zero we can increment both the low and mid after
# swapping the low and mid-values. If the mid is one we can increment mid else we swap the high and mid and decrement
# high.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1