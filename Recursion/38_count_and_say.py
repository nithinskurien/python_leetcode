# 38. Count and Say
#
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1" countAndSay(n) is the run-length encoding of countAndSay(n - 1). Run-length encoding (RLE) is
# a string compression method that works by replacing consecutive identical characters (repeated 2 or more times)
# with the concatenation of the character and the number marking the count of the characters (length of the run). For
# example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15"
# and replace "1" with "11". Thus the compressed string becomes "23321511".
#
# Given a positive integer n, return the nth element of the count-and-say sequence.
#
#
#
# Example 1:
#
# Input: n = 4
#
# Output: "1211"
#
# Explanation:
#
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:
#
# Input: n = 1
#
# Output: "1"
#
# Explanation:
#
# This is the base case.
#
#
#
# Constraints:
#
# 1 <= n <= 30
#
#
# Follow up: Could you solve it iteratively?
#
# Logic: We can initialise the base solution as curr_ans and then iteratively go till n-1 to substitute the current
# ans with next iteration. Every step we will take the curr_ans computed from the previous step and then go through
# each character and count the digits. We can then append the digit with the count and complete the curr_ans for the
# next iteration.

class Solution:
    def countAndSay(self, n: int) -> str:
        curr_ans = '1'
        for _ in range(n-1):
            next_ans = ""
            i = 0
            while i < len(curr_ans):
                count = 1
                curr_digit = curr_ans[i]
                j = i + 1
                while j < len(curr_ans) and curr_ans[j] == curr_digit:
                    count += 1
                    j += 1
                next_ans += str(count) + curr_digit
                i = j
            curr_ans = next_ans

        return curr_ans
