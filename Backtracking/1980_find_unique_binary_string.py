# 1980. Find Unique Binary String
#
# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of
# length n that does not appear in nums. If there are multiple answers, you may return any of them.
#
#
#
# Example 1:
#
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:
#
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:
#
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.
#
# Logic:
# We can first add all the nums to a set. Then we can backtrack and create the combinations of the bit numbers and check
# if it is present in the set and returning it if it is not in set.

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        num_set = set(nums)

        def backtrack(length, curr):
            if length == n:
                if not curr in num_set:
                    return curr
                return ''

            for bit in ('0', '1'):
                next = backtrack(length + 1, curr + bit)
                if next:
                    return next

        return backtrack(0, '')
