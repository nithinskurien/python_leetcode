# 3070. Count Submatrices with Top-Left Element and Sum Less Than k
#
# You are given a 0-indexed integer matrix grid and an integer k.
#
# Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal
# to k.
#
#
#
# Example 1:
#
#
# Input: grid = [[7,6,3],[6,6,1]], k = 18 Output: 4 Explanation: There are only 4 submatrices, shown in the image
# above, that contain the top-left element of grid, and have a sum less than or equal to 18. Example 2:
#
#
# Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20 Output: 6 Explanation: There are only 6 submatrices, shown in the
# image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= n, m <= 1000
# 0 <= grid[i][j] <= 1000
# 1 <= k <= 109
#
# Logic:
# We can use prefix sum to get the sum of the first row, first col and then use that to compute the prefix matrix. For
# every sum we do we can check if the sum is less than or equal to k if yes we can increment the result. 

class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        prefix_sum = [[0] * cols for _ in range(rows)]
        prefix_sum[0][0] = grid[0][0]
        if prefix_sum[0][0] <= k:
            res += 1

        for index in range(1, cols):
            prefix_sum[0][index] = grid[0][index] + prefix_sum[0][index - 1]
            if prefix_sum[0][index] <= k:
                res += 1

        for index in range(1, rows):
            prefix_sum[index][0] = grid[index][0] + prefix_sum[index - 1][0]
            if prefix_sum[index][0] <= k:
                res += 1

        for row in range(1, rows):
            for col in range(1, cols):
                prefix_sum[row][col] = grid[row][col] + prefix_sum[row - 1][col] + prefix_sum[row][col - 1] - \
                                       prefix_sum[row - 1][col - 1]
                if prefix_sum[row][col] <= k:
                    res += 1

        return res