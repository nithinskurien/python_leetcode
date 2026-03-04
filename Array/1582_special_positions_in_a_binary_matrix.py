# 1582. Special Positions in a Binary Matrix
#
# Given an m x n binary matrix mat, return the number of special positions in mat.
#
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and
# columns are 0-indexed).
#
#
#
# Example 1:
#
#
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:
#
#
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
#
# Logic:
# We can iterate the matrix and keep track of the number on ones seen in the row and col count. In the second pass we
# can for the position that has a one check if the row count and col count for that position's row and col is one each
# if yes then we can add one to the result.

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        cols = len(mat[0])
        rows = len(mat)
        res = 0
        row_ones = [0] * rows
        col_ones = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    row_ones[row] += 1
                    col_ones[col] += 1

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    if row_ones[row] == 1 and col_ones[col] == 1:
                        res += 1

        return res
