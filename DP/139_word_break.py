# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
# Algorithm Breakdown:
#
# Setup:
# wordHash = set(wordDict) - Converts the word list to a set for O(1) lookup time
from functools import cache


# dp = [False] * (len(s) + 1) - Creates a DP array where dp[i] represents whether the first i characters of string s
# can be segmented

# dp[0] = True - Empty string can always be segmented (base case)
# Dynamic Programming Logic:
# python
# for i in range(dpLength):      # For each position in the string
#     for j in range(i):         # Check all possible starting positions
#         if dp[j] and s[j:i] in wordHash:  # If substring from j to i is valid
#             dp[i] = True       # Mark position i as reachable
#             break              # No need to check further
# The key insight: dp[i] is True if there exists some position j < i where:
# dp[j] is True (first j characters can be segmented)
# s[j:i] is in the dictionary (substring from j to i is a valid word)
# Example:
#
# s = "leetcode", wordDict = ["leet", "code"]
# dp[0] = True (empty string)
# dp[4] = True because dp[0] = True and s[0:4] = "leet" is in dictionary
# dp[8] = True because dp[4] = True and s[4:8] = "code" is in dictionary
# Return dp[8] = True

# The algorithm efficiently builds up the solution by checking if each position can be reached by extending a
# previously valid segmentation with a dictionary word.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordHash = set(wordDict)
        dpLength = len(s) + 1
        dp = [False] * dpLength
        dp[0] = True
        for i in range(dpLength):
            for j in range(i):
                if dp[j] and s[j:i] in wordHash:
                        dp[i] = True
                        break
        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def wordBreakHelper(s):
            if s in wordDict:
                return True
            for word in wordDict:
                if s.startswith(word):
                    if wordBreakHelper(s[len(word):]):
                        return True
            return False
        return wordBreakHelper(s)