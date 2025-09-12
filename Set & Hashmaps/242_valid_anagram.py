# 242. Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
#
# Logic:
# We can easily just compare the counter of both words, this solution would need twice the space. Instead, for the first
# pass we can build the counter and then subtract the count and delete the key when the key becomes zero. We can then
# check if the size of the counter is zero. This will save space as only one counter is needed

from collections import Counter


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        hist = Counter(s)
        for char in t:
            if char not in hist:
                return False
            hist[char] -= 1
            if hist[char] == 0:
                del hist[char]
        return len(hist) == 0