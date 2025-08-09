# 153. Find Minimum in Rotated Sorted Array
#
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
# the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times. [0,1,2,4,5,6,7] if it was rotated 7 times. Notice that rotating an array
# [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
#
# Example 1:
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
#
# Logic: We need to find the point in the array where the value of the array is switching between increasing and
# decreasing. We initialise the start and end pointer to be the start and end of array, we then take the mid of the
# array and check if the value is greater than the end if it is the changing point or the minimum is somewhere in the
# last part. If the middle is smaller than the start then the changing point is somewhere in the start. We then update
# the end and start in every iteration to return the smallest number.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            middle = (start + end)//2
            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle
        return nums[end]