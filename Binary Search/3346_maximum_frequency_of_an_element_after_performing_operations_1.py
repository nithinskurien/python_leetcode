# 3346. Maximum Frequency of an Element After Performing Operations I
#
# You are given an integer array nums and two integers k and numOperations.
#
# You must perform an operation numOperations times on nums, where in each operation you:
#
# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,4,5], k = 1, numOperations = 2
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1]. nums becomes [1, 4, 5].
# Adding -1 to nums[2]. nums becomes [1, 4, 4].
# Example 2:
#
# Input: nums = [5,11,20,20], k = 5, numOperations = 1
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1].
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 0 <= k <= 105
# 0 <= numOperations <= nums.length
#
# Logic:
# We can sort the nums then for each possible values from the lowest number to the highest number we can check how many
# indices of the num could reach that value by doing the operations. For finding the indices that satisfy this condition
# we can use binary search to find the left most and right most indices that lie within [val-k, val+k] here we use
# bisect function to get the index of the leftmost and rightmost interval. There might be index that are already that
# value so we need to subtract that count as we do not need to use an operation as the position is already that value.
# Also we can not use more that the numOperations even when we can flip more indices to become the value.

from collections import Counter
from bisect import bisect_left, bisect_right


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        res = 0
        nums.sort()
        count = Counter(nums)

        def maxFrequency(val: int):
            left = bisect_left(nums, val - k)
            right = bisect_right(nums, val + k)
            return count[val] + min(right - left - count[val], numOperations)

        for val in range(nums[0], nums[-1] + 1):
            res = max(res, maxFrequency(val))

        return res
