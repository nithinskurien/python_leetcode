# 3634. Minimum Removals to Balance Array
#
# You are given an integer array nums and an integer k.
#
# An array is considered balanced if the value of its maximum element is at most k times the minimum element.
#
# You may remove any number of elements from nums without making it empty.
#
# Return the minimum number of elements to remove so that the remaining array is balanced.
#
# Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always
# holds true.
#
#
#
# Example 1:
#
# Input: nums = [2,1,5], k = 2
#
# Output: 1
#
# Explanation:
#
# Remove nums[2] = 5 to get nums = [2, 1].
# Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
# Example 2:
#
# Input: nums = [1,6,2,9], k = 3
#
# Output: 2
#
# Explanation:
#
# Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
# Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
# Example 3:
#
# Input: nums = [4,6], k = 2
#
# Output: 0
#
# Explanation:
#
# Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 105
#
# Logic:
# We can use 2 pointers such that we can start from each index and grow the right pointer outwards till we can satisfy
# the condition right < n and nums[right] <= nums[left] * k, for every movement of right or left we can find the length
# of the max array to be the max of right - left. At the end we can return n - result to get the removed elements.

class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            res = max(right - left, res)
            if right >= n:
                break

        return n - res

