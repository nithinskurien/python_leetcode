# 7. Reverse Integer
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
# value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
#
# Logic:
# We can reverse the string and then convert it back to int and then preserve the sign. Or we can also divide the number
# repeatedly to get the digit and then add it back to reverse the string

class Solution:
    def reverse(self, x: int) -> int:
        max = - 2**31
        min = 2**31 - 1
        if x > 0:
            a = int(str(x)[::-1])
        else:
            a = int(str(abs(x))[::-1]) * -1
        if a < max or a > min:
            return 0
        else:
            return a


class Solution2:
    def reverse(self, x: int) -> int:
        MIN_X, MAX_X = -2**31, 2**31 - 1
        reversedX = 0
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        while x:
            digit = x % 10
            reversedX = reversedX * 10 + digit
            x //= 10
        reversedX *= sign
        if MIN_X > reversedX or reversedX > MAX_X:
            return 0
        return reversedX

