# 3212. Count Submatrices With Equal Frequency of X and Y
#
# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices
# that contain:
#
# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
#
#
# Example 1:
#
# Input: grid = [["X","Y","."],["Y",".","."]]
#
# Output: 3
#
# Explanation:
#
#
#
# Example 2:
#
# Input: grid = [["X","X"],["X","Y"]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has an equal frequency of 'X' and 'Y'.
#
# Example 3:
#
# Input: grid = [[".","."],[".","."]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has at least one 'X'.
#
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.
#
# Logic:
# We can use 2 grid of prefix sums, one to keep the track of the total number of 'X' and the other for 'Y'. The prefix
# sum matrix will tell us the number of the Xs and Ys that are seen for the matrix uptil that index including the matrix
# pos[0][0]. We can then check for each of the positions the criteria of having atleast one X and the total number of
# X and Y being equal and increment the result.

class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        prefix_x = [[0] * cols for _ in range(rows)]
        prefix_y = [[0] * cols for _ in range(rows)]
        prefix_x[0][0] = (1 if grid[0][0] == 'X' else 0)
        prefix_y[0][0] = (1 if grid[0][0] == 'Y' else 0)

        for col in range(1, cols):
            prefix_x[0][col] = prefix_x[0][col - 1] + (1 if grid[0][col] == 'X' else 0)
            prefix_y[0][col] = prefix_y[0][col - 1] + (1 if grid[0][col] == 'Y' else 0)
            if prefix_x[0][col] >= 1 and prefix_x[0][col] == prefix_y[0][col]:
                res += 1

        for row in range(1, rows):
            prefix_x[row][0] = prefix_x[row - 1][0] + (1 if grid[row][0] == 'X' else 0)
            prefix_y[row][0] = prefix_y[row - 1][0] + (1 if grid[row][0] == 'Y' else 0)
            if prefix_x[row][0] >= 1 and prefix_x[row][0] == prefix_y[row][0]:
                res += 1

        for row in range(1, rows):
            for col in range(1, cols):
                prefix_x[row][col] = (1 if grid[row][col] == 'X' else 0) + prefix_x[row - 1][col] + prefix_x[row][
                    col - 1] - \
                                     prefix_x[row - 1][col - 1]
                prefix_y[row][col] = (1 if grid[row][col] == 'Y' else 0) + prefix_y[row - 1][col] + prefix_y[row][
                    col - 1] - \
                                     prefix_y[row - 1][col - 1]
                if prefix_x[row][col] >= 1 and prefix_x[row][col] == prefix_y[row][col]:
                    res += 1

        return res