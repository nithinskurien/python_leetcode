# 3719. Longest Balanced Subarray I
#
# You are given an integer array nums.
#
# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of
# distinct odd numbers.
#
# Return the length of the longest balanced subarray.
#
#
#
# Example 1:
#
# Input: nums = [2,5,4,3]
#
# Output: 4
#
# Explanation:
#
# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
# Example 2:
#
# Input: nums = [3,2,2,5,4]
#
# Output: 5
#
# Explanation:
#
# The longest balanced subarray is [3, 2, 2, 5, 4].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
# Example 3:
#
# Input: nums = [1,2,3,2]
#
# Output: 3
#
# Explanation:
#
# The longest balanced subarray is [2, 3, 2].
# It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
#
#
# Constraints:
#
# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 105
#
# Logic:
# We can go through every sub-array as the constraints allows for n^2 algorithm. For every sub-array we can store the
# value in a set and then check if the len of odd and even are equal and return the max of the length. We can also break
# the loop prematurely if we find that the result is greater than n - low as that would be the max possible and there
# would be no need to continue the iterations.

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for low in range(n):
            even_nums = set()
            odd_nums = set()
            if res > n - low:
                break
            for high in range(low, n):
                if nums[high] % 2 == 0:
                    even_nums.add(nums[high])
                else:
                    odd_nums.add(nums[high])
                if len(even_nums) == len(odd_nums):
                    res = max(res, high - low + 1)

        return res


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        seen = set()
        for i in range(n):
            seen.clear()
            balance = 0
            if res > n - i:
                break
            for j in range(i, n):
                num = nums[j]
                if num not in seen:
                    if num % 2:
                        balance -= 1
                    else:
                        balance += 1
                    seen.add(num)
                if balance == 0:
                    res = max(res, j - i + 1)

        return res
