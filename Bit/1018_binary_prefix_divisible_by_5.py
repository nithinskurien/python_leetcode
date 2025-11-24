# 1018. Binary Prefix Divisible By 5
#
# You are given a binary array nums (0-indexed).
#
# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to
# least-significant-bit).
#
# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
#
#
#
# Example 1:
#
# Input: nums = [0,1,1]
# Output: [true,false,false]
# Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
# Only the first number is divisible by 5, so answer[0] is true.
# Example 2:
#
# Input: nums = [1,1,1]
# Output: [false,false,false]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
#
# Logic:
# We can left shift each number and add the next digit to keep getting current number and append the mod of 5 to the
# result. We can mod the solution with 5 to make the number small as the remainder value does not change as left
# shifting and adding a bit functionality will preserve the remainder value. By moding the number every opertaion we
# won't overflow the given constraints.


class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        curr = 0
        res = []
        for num in nums:
            curr = ((curr << 1) + num) % 5
            res.append(curr % 5 == 0)
        return res


if __name__ == "__main__":
    print(Solution().prefixesDivBy5([1, 1, 0, 0, 0, 1, 0, 0, 1]))
