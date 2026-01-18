# 1895. Largest Magic Square
#
# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum,
# and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid
# is trivially a magic square.
#
# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be
# found within this grid.
#
#
#
# Example 1:
#
#
# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12
# Example 2:
#
#
# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 106
#
# Logic:
# We need to from each cell take the maximum possible square and then calculate the sum of each rows, cols and diagonals
# We can make use of prefix sums for each of these calculations to make the repeated computations easier. We can keep
# track of the maximum size at every iteration and return it at the end.

class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        prows = [[0] * m for _ in range(n)]
        pcols = [[0] * m for _ in range(n)]
        pd1 = [[0] * m for _ in range(n)]
        pd2 = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                prows[i][j] = curr + (prows[i][j - 1] if j > 0 else 0)
                pcols[i][j] = curr + (pcols[i - 1][j] if i > 0 else 0)
                pd1[i][j] = curr + (pd1[i - 1][j - 1] if i > 0 and j > 0 else 0)
                pd2[i][j] = curr + (pd2[i - 1][j + 1] if i > 0 and j < m - 1 else 0)

        for i in range(n):
            for j in range(m):
                for k in range(min(n - i, m - j) - 1, -1, -1):
                    # Diagonal check
                    d1 = pd1[i + k][j + k] - (pd1[i - 1][j - 1] if i > 0 and j > 0 else 0)
                    d2 = pd2[i + k][j] - (pd2[i - 1][j + k + 1] if i > 0 and j + k < m - 1 else 0)
                    if d1 != d2:
                        continue

                    # Row checks
                    valid = True
                    for row in range(i, i + k + 1):
                        if prows[row][j + k] - (prows[row][j - 1] if j > 0 else 0) != d1:
                            valid = False
                            break
                    if not valid:
                        continue

                    # Col checks
                    valid = True
                    for col in range(j, j + k + 1):
                        if pcols[i + k][col] - (pcols[i - 1][col] if i > 0 else 0) != d1:
                            valid = False
                            break
                    if not valid:
                        continue

                    res = max(res, k + 1)
                    break

        return res