# 2598. Smallest Missing Non-negative Integer After Operations
#
# You are given a 0-indexed integer array nums and an integer value.
#
# In one operation, you can add or subtract value from any element of nums.
#
# For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
# The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.
#
# For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
# Return the maximum MEX of nums after applying the mentioned operation any number of times.
#
#
#
# Example 1:
#
# Input: nums = [1,-10,7,13,6,8], value = 5
# Output: 4
# Explanation: One can achieve this result by applying the following operations:
# - Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
# - Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
# - Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
# The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
# Example 2:
#
# Input: nums = [1,-10,7,13,6,8], value = 7
# Output: 2
# Explanation: One can achieve this result by applying the following operation:
# - subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
# The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
#
#
# Constraints:
#
# 1 <= nums.length, value <= 105
# -109 <= nums[i] <= 109
#
# Logic:
# We can make a counter with the remainders of the nums. The remainder is the more important as the nums could be broken
# down to their remainder by repeated operations. Once we have the counter of remainders we can initialise the mex as 0
# and then check if the remainder of mex with value exists in the counter if it does we can reduce the counter and then
# increase the mex and keep going till the counter does not have the remainder of mex with value. If we see that the
# count does not exist it means we cannot create that mex by repeated operations.


from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        count = Counter(x % value for x in nums)
        mex = 0
        while count[mex % value] > 0:
            count[mex % value] -= 1
            mex += 1
        return mex
