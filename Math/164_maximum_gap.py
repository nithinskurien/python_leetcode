# 164. Maximum Gap
#
# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If
# the array contains less than two elements, return 0.
#
# You must write an algorithm that runs in linear time and uses linear extra space.
#
#
#
# Example 1:
#
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
# Example 2:
#
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
#
# Logic:
# The key insight is that the maximum gap must be at least as large as the average gap. By placing numbers
# into buckets, we can:
#
# Skip checking gaps within buckets (they're smaller than average)
# Only check gaps between buckets (where the maximum gap must be)
#
from cmath import inf


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums)

        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        buckets = [[inf, -inf] for _ in range(bucket_count)]

        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        prev_max = inf

        for i in range(bucket_count):
            if buckets[i][0] == inf:
                continue
            if prev_max == inf:
                prev_max = buckets[i][1]
                continue
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]

        return max_gap
