# Q1. Set Mismatch
#
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some
# error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one
# number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104
#
# Logic:
# We add the nums to counter and then iterate over the range of 1 to n and check if the num is in the map and if it
# occurs more than once and then return both the values.

from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        num_map = Counter(nums)
        duplicate_num = 0
        missing_num = 0
        for num in range(1, len(nums) + 1):
            if num not in num_map:
                missing_num = num
            if num_map[num] > 1:
                duplicate_num = num
        return [duplicate_num, missing_num]
