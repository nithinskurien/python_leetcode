# 647. Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
#
# Example 1:
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
# Logic: We need to start from a character and start moving outwards to the left and right and check if the
# characters are equal on both sides, we continue to do so until they are not. We can then update the count of found
# palindrome. There are 2 scenarios where we need to do this check one where we are at a character and once when we
# are between two characters as if we have a str with odd characters the middle is a character but in an even case we
# have the middle in between 2 characters. For the checking in the middle case it only needs to be done when the
# current and next characters are equal. So we can iterate over the whole string and return the count in the end


class Solution:

    def __init__(self):
        self.s = ""

    def isPalindrome(self, left: int, right: int) -> int:
        count = 1
        while left > 0 and right < len(self.s) - 1 and self.s[left - 1] == self.s[right + 1]:
            left -= 1
            right += 1
            count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        self.s = s
        maxCount = 1
        for index in range(len(self.s) - 1):
            maxCount += self.isPalindrome(index, index)
            if self.s[index] == self.s[index + 1]:
                maxCount += self.isPalindrome(index, index + 1)
        return maxCount


if __name__ == "__main__":
    print(Solution().countSubstrings("abc"))
