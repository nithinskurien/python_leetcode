# 28. Find the Index of the First Occurrence in a String
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
#
#
# Example 1:
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
# Constraints:
#
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
#
# Logic:
# We can use 2 pointers to traverse the haystack and needle (1 each). We can iterate over the haystack and needle till
# we reach the end of the array. Then within the loop we can check if the character at the pointer are the same if the
# len of the pointers after the internal loop is the same we can say that the index is found.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = j = 0
        while i < len(haystack) and j < len(needle):
            start = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return start
            i = start + 1
            j = 0
        return -1
