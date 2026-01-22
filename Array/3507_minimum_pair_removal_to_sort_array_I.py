# 3507. Minimum Pair Removal to Sort Array I
#
# Given an array nums, you can perform the following operation any number of times:
#
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
#
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
#
# Output: 2
#
# Explanation:
#
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.
#
# Example 2:
#
# Input: nums = [1,2,2]
#
# Output: 0
#
# Explanation:
#
# The array nums is already sorted.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000
#
# Logic: We can iterate the list over and over till the array is sorted. For every pass of the array we can find the
# lowest adjacent sum and the index of the sum. If the array is not sorted for any of the adjacent values we can mark
# the array to not be sorted and then change the array by using the index and summing up the lowest sum index,
# incrementing the result. Once the array is sorted we return the result.


class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        res = 0

        while True:
            is_sorted = True
            min_sum = float('inf')
            min_idx = -1

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i

                if nums[i + 1] < nums[i]:
                    is_sorted = False

            if is_sorted:
                break

            nums = nums[:min_idx] + [min_sum] + nums[min_idx + 2:]
            res += 1

        return res

