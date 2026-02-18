# 693. Binary Number with Alternating Bits
#
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have
# different values.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
#
# Constraints:
#
# 1 <= n <= 231 - 1
#
# Logic:
# We can xor the alternating bits and if any of the result is zero we can return False else return True. For XORing the
# alternate bits we can right shift and AND with one to get the last bit and keep doing it to get the alternate bits.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        old = n & 1
        while n > 0:
            n >>= 1
            new = n & 1
            if old ^ new == 0:
                return False
            old = new
        return True