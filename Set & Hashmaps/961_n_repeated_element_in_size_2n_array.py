# 961. N-Repeated Element in Size 2N Array
#
# You are given an integer array nums with the following properties:
#
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,1,2,5,3,2]
# Output: 2
# Example 3:
#
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5
#
#
# Constraints:
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums contains n + 1 unique elements and one of them is repeated exactly n times.
#
# Logic:
# As the constraints are that the length of nums is 2N, with N + 1 unique elements with one element being repeated N
# times we can safely assume that when iterating the array if we were to encounter an element previously seen we can
# be sure that it is the repeated element which will be repeated N times, so we can already terminate the check and
# return the element.

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)