# 33. Search in Rotated Sorted Array
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (
# 0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in
# nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
#
# Logic:
# We need to split the array to the sorted part and the rotated part, then we will use binary search in each of the
# section to find the target.

class Solution:
    class Solution:
        def search(self, nums: list[int], target: int) -> int:
            start, end = 0, len(nums) - 1
            mid = 0
            while start < end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                if nums[start] <= nums[mid]:
                    if nums[start] <= target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if nums[mid] < target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1 if nums[end] != target else end


if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
