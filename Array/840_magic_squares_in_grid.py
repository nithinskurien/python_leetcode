# 840. Magic Squares In Grid
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
# and both diagonals all have the same sum.
#
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?
#
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
#
#
#
# Example 1:
#
#
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
#
# while this one is not:
#
# In total, there is only one magic square inside the given grid.
# Example 2:
#
# Input: grid = [[8]]
# Output: 0
#
#
# Constraints:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
#
# Logic:
# We can write a function that accepts a row and col and checks if the matrix with those upper bounds is valid by
# simulating all the constraints. We can then iterate from 2 to rows and col count to get the sub matrices. We can then
# increment a variable when each sub matrices are valid.

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def valid(row, col):
            nums = set()
            for m in range(row - 2, row + 1):
                for n in range(col - 2, col + 1):
                    if grid[m][n] in nums:
                        return False
                    nums.add(grid[m][n])
            left_diagonal = grid[row - 2][col - 2] + grid[row - 1][col - 1] + grid[row][col]
            right_diagonal = grid[row - 2][col] + grid[row - 1][col - 1] + grid[row][col - 2]
            if left_diagonal != right_diagonal:
                return False

            for m in range(row - 2, row + 1):
                if grid[m][col - 2] + grid[m][col - 1] + grid[m][col] != left_diagonal:
                    return False

            for n in range(col - 2, col + 1):
                if grid[row - 2][n] + grid[row - 1][n] + grid[row][n] != left_diagonal:
                    return False

            return nums == set(range(1, 10))

        for row in range(2, rows):
            for col in range(2, cols):
                if valid(row, col):
                    res += 1

        return res