# 1351. Count Negative Numbers in a Sorted Matrix
#
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number
# of negative numbers in grid.
#
#
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
#
#
# Follow up: Could you find an O(n + m) solution?
#
# Logic:
# Given that the numbers are non-increasing both in the row and col we can use that information to have 2 pointers for
# the row and col set at 0 and max col initially. We can then check if the element in the first row last column is less
# than one if that is the case then all the elements below that column will be less than zero, so we can increment the
# result by the number of rows and decrement the col, if the number is not less than zero we can increment the row
# pointer and check.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row, col, res = 0, cols - 1, 0
        while row < rows and col >= 0:
            if grid[row][col] < 0:
                res += rows - row
                col -= 1
            else:
                row += 1
        return res