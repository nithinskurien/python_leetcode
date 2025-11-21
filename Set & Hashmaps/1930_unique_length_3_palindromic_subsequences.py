# 1930. Unique Length-3 Palindromic Subsequences
#
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 105
# s consists of only lowercase English letters.
#
# Logic:
# We are trying to find 3 character length strings where a middle character is surrounded by similar characters. We can
# split the array into 3 a left set (we are always adding elements to it) a middle single character and a right hashmap
# (we will be removing characters so set will not work). Now we can iterate over the characters in the string such that
# we will keep removing the character from the right map and then for each char in the left set see if the same exists
# in the right map. If yes we will add it to a set. We will later return the length of the result set

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)
        for mid in s:
            right[mid] -= 1
            for char in left:
                if right[char] > 0:
                    res.add((char, mid))
            left.add(mid)
        return len(res)