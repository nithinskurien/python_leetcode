# 128. Longest Consecutive Sequence
#
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
#
# Input: nums = [1,0,1,2]
# Output: 3
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
#
# Logic:
# As we need to do the computation in O(n) time complexity we can use more space to achieve this. We can create a set of
# the input and loop through the set, the number needs to be the start of the sequence to reduce the search space, so we
# can check if the previous number exists in the set if it does not we can start to look for the next consecutive number
# in a loop using set lookup in constant time if found we increase the length of max found numbers and continue for all
# the numbers in the set.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                currSum = 1
                nextNum = num + 1
                while nextNum in numSet:
                    currSum += 1
                    nextNum += 1
                longest = max(longest, currSum)
        return longest