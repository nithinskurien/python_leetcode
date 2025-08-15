# 49. Group Anagrams
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
# Logic:
# We can loop through the list and every time we encounter a word we can sort it based on it's alphabets, we can then
# append to the list corresponding to a dict that has the key as the sorted array.


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        resultDict = defaultdict(list)
        for string in strs:
            sortedString = "".join(sorted(string))
            resultDict[sortedString].append(string)
        return list(resultDict.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
