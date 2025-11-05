# 67. Add Binary
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
# Logic:
# We can first reverse the str as we want the add the LSB first, we initialise the carry as 0 and res as empty. We can
# then iterate index from 0 to max(len(a), len(b)) exclusive. The get the digit of a & b. If the index is more than what
# the str has we use 0 instead. We get the total for the bit as digit_a + digit_b + carry and add the remainder of total
# with res and set the carry as total // 2. We do this for the whole a & b. In the end we need to check if there is a
# carry over if so add the 1 to the res.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for index in range(max(len(a), len(b))):
            digit_a = int(a[index]) if index < len(a) else 0
            digit_b = int(b[index]) if index < len(b) else 0

            total = digit_a + digit_b + carry
            res = str(total % 2) + res
            carry = total // 2

        if carry:
            res = '1' + res

        return res