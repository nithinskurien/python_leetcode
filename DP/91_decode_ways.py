# 91. Decode Ways
#
# You have intercepted a secret message encoded as a string of numbers. The message is decoded via
# the following mapping:
#
# "1" -> 'A'
#
# "2" -> 'B'
#
# ...
#
# "25" -> 'Y'
#
# "26" -> 'Z'
#
# However, while decoding the message, you realize that there are many different ways you can decode the message
# because some codes are contained in other codes ("2" and "5" vs "25").
#
# For example, "11106" can be decoded into:
#
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.
#
# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be
# decoded in any valid way, return 0.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: s = "12"
#
# Output: 2
#
# Explanation:
#
# "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: s = "226"
#
# Output: 3
#
# Explanation:
#
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
#
# Input: s = "06"
#
# Output: 0
#
# Explanation:
#
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is
# not a valid encoding, so return 0.
#
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
#
# Logic:
# We will split the problems into sub problems and solve it dynamically. We know that to choose no number from string
# there is 1 way so is when we choose one number from the string. We will then check from the second number in string.
# We will check if the number is not zero if it not we increment the ways we can get this by the previous dp solution.
# We can now check if the double-digit number formed by the combination of the current number with previous number lies
# within 10 and 26 inclusive, if it does then we can add the ways with the ways array index - 2. We can then return the
# last index value.

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [1, 1]
        for index, num in enumerate(s[1:], 2):
            ways = 0
            if num != '0':
                ways += dp[index - 1]
            if 10 <= int(s[index - 2] + num) <= 26:
                ways += dp[index - 2]
            dp.append(ways)
            print(num)
        return dp[-1]
