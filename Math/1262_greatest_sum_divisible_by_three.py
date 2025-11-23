# 1262. Greatest Sum Divisible by Three
#
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by
# three.
#
#
#
# Example 1:
#
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:
#
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:
#
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
#
#
# Constraints:
#
# 1 <= nums.length <= 4 * 104
# 1 <= nums[i] <= 104
#
# Logic: We can use the greedy approach to first assume the largest number is the sum of all the numbers. If that is
# not divisible by 3 we need to find the smallest number that when subtracted from the total would give a number
# divisible by 3. We have 2 options, either remove a num (or sum of nums) that has a remainder of 1 or remainder of 2
# based on what is the remainder of the total. Sometimes a sum of numbers with remainder 1 can be formed by adding
# numbers with remainder 2 and vice-versa. So we need to keep track of the minimum for both smallest_one and
# smallest_two.


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        smallest_one = float('inf')
        smallest_two = float('inf')
        total = 0
        for num in nums:
            total += num
            if num % 3 == 1:
                smallest_two = min(smallest_two, num + smallest_one)
                smallest_one = min(smallest_one, num)
            if num % 3 == 2:
                smallest_one = min(smallest_one, num + smallest_two)
                smallest_two = min(smallest_two, num)

        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            return total - smallest_one
        else:
            return total - smallest_two