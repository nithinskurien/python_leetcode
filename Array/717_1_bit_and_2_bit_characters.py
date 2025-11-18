# 717. 1-bit and 2-bit Characters
#
# We have two special characters:
#
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
#
#
#
# Example 1:
#
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:
#
# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.
#
#
# Constraints:
#
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.
#
# Logic:
# We can iterate over the array and when we encounter a 1 we can iterate the index by one as 1 is part of the 2 bit
# character. If the bit is one we can check after the increment if the index is the last index if yes then we can return
# false. If we complete the loop then we return True.


class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        index = 0
        while index < len(bits):
            if bits[index] == 1:
                index +=1
                if index == len(bits) - 1:
                    return False
            index +=1
        return True


if __name__ == "__main__":
    print(Solution().isOneBitCharacter([1, 1, 1, 0]))
