# 3349. Adjacent Increasing Subarrays Detection I
#
# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length
# k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at
# indices a and b (a < b), where:
#
# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
#
# Output: true
#
# Explanation:
#
# The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
# The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
# These two subarrays are adjacent, so the result is true.
# Example 2:
#
# Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
#
# Output: false
#
#
#
# Constraints:
#
# 2 <= nums.length <= 100
# 1 < 2 * k <= nums.length
# -1000 <= nums[i] <= 1000
#
# Logic:
# We can from every position in the array take a sub array of k and the consecutive array of k and then check if both of
# them are strictly increasing. We can return True if both are valid. We can iterate over the array to check all the
# possibilities and return false if we have exhausted all the options.

class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:

        if len(nums) < 2 * k:
            return False

        if k == 1:
            return True

        def is_strictly_increasing(sub_array: list[int]) -> bool:
            for index in range(len(sub_array) - 1):
                if sub_array[index] >= sub_array[index + 1]:
                    return False
            return True

        for index in range(len(nums) - 2 * k + 1):
            sub_array_1 = nums[index: index + k]
            sub_array_2 = nums[index + k: index + 2 * k]

            if is_strictly_increasing(sub_array_1) and is_strictly_increasing(sub_array_2):
                return True

        return False


if __name__ == "__main__":
    print(Solution().hasIncreasingSubarrays([5, 8, -2, -1], 2))
