# 190. Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output
# will be given as a signed integer type. They should not affect your implementation, as the integer's internal
# binary representation is the same, whether it is signed or unsigned. In Java, the compiler represents the signed
# integers using 2's complement notation.
#
#
# Example 1:
#
# Input: n = 43261596
#
# Output: 964176192
#
# Explanation:
#
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:
#
# Input: n = 2147483644
#
# Output: 1073741822
#
# Explanation:
#
# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
#
#
# Constraints:
#
# 0 <= n <= 231 - 2
# n is even.
#
#
# Follow up: If this function is called many times, how would you optimize it?
#
# Logic:
# we will take the last bit of the number and add it to the result initialised to zero and left shifted. The number is
# then right shifted to get the next bit and the cycle continues 32 times to return the result

class Solution:
    def reverseBits(self, n: int) -> int:
        reversedN = 0
        for _ in range(32):
            reversedN = (reversedN << 1) | (n & 1)
            n >>= 1
        return reversedN