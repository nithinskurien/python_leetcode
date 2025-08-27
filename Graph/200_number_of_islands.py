#
#
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of
# islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
# Logic:
# We loop through the matrix and if the position is land we do a dfs by converting the land to water to mark the land
# was visited. We can then check on all four directions and see if there is land and if yes do a dfs. We will return to
# the original call once we have found and island. As we have marked all seen land as water in the main loop we will go
# to the not visited land and continue the process to find a new island. We will keep track of the islands found in the
# main loop and return the answer in the end.


class Solution:

    def __init__(self):
        self.grid = None

    def dfs(self, row, col):
        self.grid[row][col] = '0'
        directions = [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]
        for r, c in directions:
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == '1':
                self.dfs(r, c)

    def numIslands(self, grid: list[list[str]]) -> int:
        island = 0
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(row, col)
                    island += 1
        return island
