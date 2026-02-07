# 1653. Minimum Deletions to Make String Balanced
#
# You are given a string s consisting only of characters 'a' and 'b'.
#
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,
# j) such that i < j and s[i] = 'b' and s[j]= 'a'.
#
# Return the minimum number of deletions needed to make s balanced.
#
#
#
# Example 1:
#
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:
#
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.
#
# Logic:
# Solution 1:
#
# For every index i, treat it as the boundary:
#
# [a ... a | b ... b]
#           ^
#         index i
#
#
# To make this happen:
#
# Delete all 'b's to the left
#
# Delete all 'a's to the right
#
# Total deletions at index i:
#
# prefix_b[i] + suffix_a[i]
#
#
# Take the minimum over all i.
#
# Solution 2:
#
# Key idea (high level)
#
# When we scan the string left to right:
#
# Seeing a 'b' is fine — it might stay.
#
# Seeing an 'a' after a 'b' causes a conflict.
#
# At that point we have two choices:
#
# Delete this 'a'
#
# Delete one of the previous 'b's
#
# This algorithm greedily picks the cheaper option as it goes.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        count = 0
        for ch in s:
            if ch == 'b':
                count += 1
            elif count:
                res += 1
                count -= 1

        return res


class Solution2:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        res = float('inf')
        suffix_a = [0] * n
        prefix_b = [0] * n
        for index in range(1, n):
            prefix_b[index] = prefix_b[index - 1] + (1 if s[index - 1] == 'b' else 0)

        for index in range(n - 2, -1, -1):
            suffix_a[index] = suffix_a[index + 1] + (1 if s[index + 1] == 'a' else 0)

        for index in range(n):
            res = min(res, prefix_b[index] + suffix_a[index])

        return res