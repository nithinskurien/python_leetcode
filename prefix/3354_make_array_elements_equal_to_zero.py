# 3354. Make Array Elements Equal to Zero
#
# You are given an integer array nums.
#
# Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either
# left or right.
#
# After that, you repeat the following process:
#
# If curr is out of the range [0, n - 1], this process ends. If nums[curr] == 0, move in the current direction by
# incrementing curr if you are moving right, or decrementing curr if you are moving left. Else if nums[curr] > 0:
# Decrement nums[curr] by 1. Reverse your movement direction (left becomes right and vice versa). Take a step in your
# new direction. A selection of the initial position curr and movement direction is considered valid if every element
# in nums becomes 0 by the end of the process.
#
# Return the number of possible valid selections.
#
#
#
# Example 1:
#
# Input: nums = [1,0,2,0,3]
#
# Output: 2
#
# Explanation:
#
# The only possible valid selections are the following:
#
# Choose curr = 3, and a movement direction to the left. [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,
# 3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,
# 0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0]. Choose curr = 3,
# and a movement direction to the right. [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,
# 2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,
# 0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0]. Example 2:
#
# Input: nums = [2,3,4,0,4,1,0]
#
# Output: 0
#
# Explanation:
#
# There are no possible valid selections.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# There is at least one element i where nums[i] == 0.
#
# Logic:
# We could solve the problem using simulation but that would take very long, the optimal solution is to, at a zero check
# what is the sum of values to the left and the right if they are equal we can start traversing both directions as the
# direction can bounce back and forth till all the elements are set to zero. If the difference between left and right is
# one then only one direction is valid as only the start towards the larger sum will result in all the elements becoming
# zero. For any other case the array cannot become zero.


class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = 0
        for index in range(n):
            right_sum = total_sum - left_sum
            if nums[index] == 0:
                if right_sum == left_sum:
                    ans += 2
                elif abs(left_sum - right_sum) == 1:
                    ans += 1
            left_sum += nums[index]
        return ans


if __name__ == "__main__":
    print(Solution().countValidSelections([1, 0, 2, 0, 3]))
