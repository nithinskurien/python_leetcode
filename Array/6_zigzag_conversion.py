# 6. Zigzag Conversion
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
# display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
# Logic:
# We can initialise an array of empty strings of length numRows. We can for each character append to the index of the
# empty string array based on what step it is in. We can then either increase the step or reduce the step based on where
# we are in the zig zag journey. We can then join all the rows as a string and return the value.



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row, step = 0, 1

        for ch in s:
            rows[cur_row] += ch
            # Change direction at top or bottom row
            if cur_row == 0:
                step = 1
            elif cur_row == numRows - 1:
                step = -1
            cur_row += step

        return "".join(rows)