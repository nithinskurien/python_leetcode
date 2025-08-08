# 152. Maximum Product Subarray
#
# Given an integer array nums, find a subarray that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
#
# Logic:
# This effectively captures the max product subarray from both directions because:
#
# Multiplying cumulatively handles contiguous subarrays.
#
# Reversing and doing the same ensures you catch subarrays starting from the right side.
#
# Zero resets multiplication chains implicitly, because you skip multiplication when the previous number is zero.


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums_reversed = nums[::-1]

        for i in range(1, len(nums)):
            if nums[i - 1] != 0:
                nums[i] *= nums[i - 1]

            if nums_reversed[i - 1] != 0:
                nums_reversed[i] *= nums_reversed[i - 1]

        return max(nums + nums_reversed)

# Logic:
# You maintain the max and min product ending at each position.
#
# This accounts for sign flips caused by negatives.
#
# Keep track of the global max product.
#
# The solution runs in O(n) time with O(1) extra space.
#


class Solution2:
    def maxProduct(self, nums: list[int]) -> int:
        maxProduct = currMaxProduct = currMinProduct = nums[0]
        for num in nums[1:]:
            temp = currMaxProduct
            currMaxProduct = max(num, num * currMinProduct, num * currMaxProduct)
            currMinProduct = min(num, num * currMinProduct, num * temp)
            maxProduct = max(currMaxProduct, maxProduct)
        return maxProduct
