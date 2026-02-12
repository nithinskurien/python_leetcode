# 3713. Longest Balanced Substring I
#
# You are given a string s consisting of lowercase English letters.
#
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
#
# Return the length of the longest balanced substring of s.
#
#
#
# Example 1:
#
# Input: s = "abbac"
#
# Output: 4
#
# Explanation:
#
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
#
# Example 2:
#
# Input: s = "zzabccy"
#
# Output: 4
#
# Explanation:
#
# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly
# 1 time.
#
# Example 3:
#
# Input: s = "aba"
#
# Output: 2
#
# Explanation:
#
# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1
# time. Another longest balanced substring is "ba".
#
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
# Logic:
# We can check all the possible combinations of substring and get the frequency of the characters. We can then put the
# values into a set if all the frequencies are the same we can say the characters are balanced and the size of such a
# set would be one. If we get a substring with satisfies such a criteria we can replace the result by the max of the
# result and the length of such a substring.

from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        n = len(s)
        for start in range(n):
            char_map = defaultdict(int)
            if res > n - start:
                break
            for end in range(start, n):
                char_map[s[end]] += 1
                if len(set(char_map.values())) == 1:
                    res = max(res, end - start + 1)

        return res