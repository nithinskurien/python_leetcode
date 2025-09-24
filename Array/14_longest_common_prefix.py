# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
#
# Logic:
# We can assign the prefix to be the first element of the strings array. We can then for each index in the prefix check
# for every word in the array if the character is the same or if the length of the word is at the current index if it is
# so then we can return the partial word of the prefix from the start to the index non inclusive.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for index in range(len(prefix)):
            for word in strs:
                if index == len(word) or prefix[index] != word[index]:
                    return prefix[:index]
        return prefix