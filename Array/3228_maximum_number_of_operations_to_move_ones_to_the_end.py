# 3228. Maximum Number of Operations to Move Ones to the End
#
# You are given a binary string s.
#
# You can perform the following operation on the string any number of times:
#
# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'. Move the
# character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010",
# if we choose i = 1, the resulting string will be s = "000110". Return the maximum number of operations that you can
# perform.
#
#
#
# Example 1:
#
# Input: s = "1001101"
#
# Output: 4
#
# Explanation:
#
# We can perform the following operations:
#
# Choose index i = 0. The resulting string is s = "0011101".
# Choose index i = 4. The resulting string is s = "0011011".
# Choose index i = 3. The resulting string is s = "0010111".
# Choose index i = 2. The resulting string is s = "0001111".
# Example 2:
#
# Input: s = "00111"
#
# Output: 0
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
#
# Logic:
# We need to have a greedy approach of trying to move the first ones to the end so that we do not close the zeroes to
# the end of the string for e.g. in "1001101" if we use 2 operations to close the last zero "1000111" we have lost the
# chance to move the ones through that zero. So to maximise the operations we need to move the ones from the start. So
# we can keep count of the ones we have seen till we reach a zero. Once we reach a zero we can add the ones we have seen
# to the result and continue till we have seen all the zeroes and have reached the end of the string.


class Solution:
    def maxOperations(self, s: str) -> int:
        one_count = 0
        res = 0
        index = 0
        while index < len(s):
            if s[index] == '1':
                one_count += 1
                index += 1
            else:
                while index < len(s) and s[index] == '0':
                    index += 1
                res += one_count
        return res