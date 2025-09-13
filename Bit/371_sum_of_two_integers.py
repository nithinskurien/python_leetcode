# 371. Sum of Two Integers
#
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
#
#
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
# -1000 <= a, b <= 1000
#
# Logic:
# We can divide the sum into 2 steps, one is adding the bits of 2 numbers using XOR and carrying over the carry to the
# left and adding it. We can continue this process till there is no more carry left. We need to also truncate the
# solution to only 32 bits or the solution will timeout. So we use a 32 bit mask to truncate the solution so that we can
# bind the carry.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask & b) > 0:
            a, b = a ^ b, (a & b) << 1
        return (mask & a) if b > 0 else a