# 300. Longest Increasing Subsequence
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
#
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
#
# Logic:
# Algorithm: Longest Increasing Subsequence (O(n log n) version)
#
# Keep an array (sequence) with the length of the correct sequence
#
# This array does not store the actual subsequence, just the best possible “endings” to keep the door open for longer
# subsequences later. So we will replace the subsequence with smaller encountered numbers to allow for the sequence to
# grow
#
# Go through the numbers one by one:
#
# If the current number is greater than the last number in sequence, it means we can make a longer subsequence — so
# append it.
#
# Otherwise, find the first sequence in tails that is greater than or equal to the current number and replace it with
# the current number.
#
# This makes the subsequence ending as small as possible, which helps build longer subsequences later.
#
# At the end, the length of sequence is the length of the longest increasing subsequence.


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sequence = [nums[0]]
        length = 1
        for num in nums:
            if sequence[-1] < num:
                sequence.append(num)
                length += 1
            else:
                left, right = 0, len(sequence) - 1
                while left < right:
                    mid = (left + right) // 2
                    if sequence[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                sequence[left] = num
        return length

