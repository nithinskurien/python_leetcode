# Given a string s, return the longest palindromic substring in s.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
# Logic: We need to start from a character and start moving outwards to the left and right and check if the
# characters are equal on both sides, we continue to do so until they are not. We can then update the left,
# right and length of the found palindrome. There are 2 scenarios where we need to do this check one where we are at
# a character and once when we are between two characters as if we have a str with odd characters the middle is a
# character but in an even case we have the middle in between 2 characters. For the checking in the middle case it
# only needs to be done when the current and next characters are equal. So we can iterate over the whole string and
# return the substring between the left and right pointers.


class Solution:

    def __init__(self):
        self.s = ""

    def isPalindrome(self, left: int, right: int) -> (int, int, int):
        while left > 0 and right < len(self.s) - 1 and self.s[left - 1] == self.s[right + 1]:
            left -= 1
            right += 1
        return left, right, right - left + 1

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        maxLeft = 0
        maxRight = 0
        maxLength = 0
        for index in range(len(self.s) - 1):
            left, right, length = self.isPalindrome(index, index)
            if length > maxLength:
                maxLeft, maxRight, maxLength = left, right, length
            if self.s[index] == self.s[index + 1]:
                left, right, length = self.isPalindrome(index, index + 1)
                if length > maxLength:
                    maxLeft, maxRight, maxLength = left, right, length
        return self.s[maxLeft:maxRight + 1]


if __name__=="__main__":
    print(Solution().longestPalindrome("cbbd"))
