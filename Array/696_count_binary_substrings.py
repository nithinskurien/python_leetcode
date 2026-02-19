# 696. Count Binary Substrings
#
# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
#
#
# Example 1:
#
# Input: s = "00110011" Output: 6 Explanation: There are 6 substrings that have equal number of consecutive 1's and
# 0's: "0011", "01", "1100", "10", "0011", and "01". Notice that some of these substrings repeat and are counted the
# number of times they occur. Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped
# together. Example 2:
#
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
#
# Logic:
# We can group the bits int consecutive numbers for e.g in 00110011 we can convert this to [2, 2, 2, 2] indicating the
# groupings of 0s and 1s. Once we have these grouping the substrings we can make of 2 sets of grouping is min(groupA,
# groupB) i.e. for 0011 the substrings possible are 0011 and 01. So we can iterate the grouped number array and return
# the result.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        temp = 0
        club_array = []
        current = -1
        for char in s:
            if char == current:
                temp += 1
            else:
                club_array.append(temp)
                current = char
                temp = 1
        if temp:
            club_array.append(temp)

        for index in range(1, len(club_array)):
            res += min(club_array[index], club_array[index - 1])

        return res