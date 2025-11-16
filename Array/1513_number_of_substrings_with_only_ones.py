# 1513. Number of Substrings With Only 1s
#
# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too
# large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# Example 2:
#
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
# Example 3:
#
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
#
# Logic:
# For a continuous substing of ones e.g 111 the number of substring will be n * (n + 1) / 2 (one for each ones, two for
# the doubles and one for the triple (3 + 2 + 1)) So we can find the continuity of ones and add it to the result.


class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        cont = 0
        for c in s:
            if c == '1':
                cont += 1
                res = (res + cont) % (10**9 + 7)
            else:
                cont = 0
        return res
