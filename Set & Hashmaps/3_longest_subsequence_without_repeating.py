# Given a string s, find the length of the longest substring without duplicate characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
#
# Logic: Have 2 pointers move including characters to create the sequence. We keep track of the count of digits in
# the current subsequence using a hash map. First the pointers will start at 0 and the end pointer will start
# including the characters one by one till the hashmap count for the end pointer character becomes more than 1. We
# can then reduce the start pointer till the count becomes 1 again, after which the end pointer can start to move
# till it reaches the end. Every time the character count for the sequence is one we will measure the max length and
# then return it at the end.

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        startPointer = 0
        endPointer = 0
        hashmap = defaultdict(int)
        while endPointer < len(s):
            currEnd = s[endPointer]
            if hashmap[currEnd] > 1:
                hashmap[s[startPointer]] -= 1
                startPointer += 1
            else:
                hashmap[currEnd] += 1
            if hashmap[currEnd] == 1:
                endPointer += 1
                maxLength = max(maxLength, endPointer - startPointer)
        return maxLength


if __name__=="__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))