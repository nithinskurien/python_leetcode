# 191. Number of 1 Bits
#
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also
# known as the Hamming weight).
#
#
#
# Example 1:
#
# Input: n = 11
#
# Output: 3
#
# Explanation:
#
# The input binary string 1011 has a total of three set bits.
#
# Example 2:
#
# Input: n = 128
#
# Output: 1
#
# Explanation:
#
# The input binary string 10000000 has a total of one set bit.
#
# Example 3:
#
# Input: n = 2147483645
#
# Output: 30
#
# Explanation:
#
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
#
#
#
# Constraints:
#
# 1 <= n <= 231 - 1
#
#
# Follow up: If this function is called many times, how would you optimize it?
#
# Logic:
# We can count the ones by looking at the last bit and seeing if it is one and if yes increment the count. We can then
# right shift the number and check the last bit again and continue till the number is not zero.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count