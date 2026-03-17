# 1727. Largest Submatrix With Rearrangements
#
# You are given a binary matrix of size m x n, and you are allowed to rearrange the columns of the matrix in
# any order.
#
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering
# the columns optimally.
#
#
#
# Example 1:
#
#
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# Example 2:
#
#
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# Example 3:
#
# Input: matrix = [[1,1,0],[1,0,1]] Output: 2 Explanation: Notice that you must rearrange entire columns,
# and there is no way to make a submatrix of 1s larger than an area of 2.
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
# matrix[i][j] is either 0 or 1.
#
# Logic:
# Treat each row as the base of a histogram: build heights[j] = consecutive 1s in column j up to current row.
#
# For each row, sort these heights in descending order to simulate rearranging columns optimally.
#
# Compute possible areas using height × width where width = number of columns considered (j+1).
#
# Track and return the maximum area found across all rows.

class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            # build heights
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] else 0
            # sort heights in descending order to simulate column reordering
            sorted_heights = sorted(heights, reverse=True)
            for j in range(n):
                max_area = max(max_area, sorted_heights[j] * (j + 1))
        return max_area
