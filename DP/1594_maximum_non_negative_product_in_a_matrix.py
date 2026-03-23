# 1594. Maximum Non Negative Product in a Matrix
#
# You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step,
# you can only move right or down in the matrix.
#
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1,
# n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers
# in the grid cells visited along the path.
#
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.
#
# Notice that the modulo is performed after getting the maximum product.
#
#
#
# Example 1:
#
#
# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
# Example 2:
#
#
# Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
# Example 3:
#
#
# Input: grid = [[1,3],[0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# -4 <= grid[i][j] <= 4
#
# Logic: Step 1: The "Two-Value" Strategy In a simple addition-based grid, you only care about the maximum. But with
# multiplication, a negative number can flip a tiny minimum into a huge maximum.
#
# Example: If you are at a cell with -10 and your neighbor says their minimum is -50, you just found a product of 500!
#
# Rule: Every recursive call must return both the Maximum and Minimum product possible from that cell to the end.
#
# Step 2: The Recursive Call (i, j)
# When we are at cell (i, j), we look at our two possible moves:
#
# Move Down: Call dp(i + 1, j). It returns (max_down, min_down).
#
# Move Right: Call dp(i, j + 1). It returns (max_right, min_right).
#
# We multiply our current cell value grid[i][j] by all four of those results. From those four products, we pick the
# new absolute maximum and absolute minimum for our current cell.
#
# Step 3: Base Cases (The Stopping Points) The Destination: If we reach the bottom-right corner (m-1, n-1),
# the max and min are just the value of that cell itself.
#
# The Boundaries: If we step outside the grid (e.g., i >= m), we return values that won't interfere with our max()
# and min() calculations (usually None or handled by logic).
#
# Step 4: Memoization (The Memory) Without memoization, the recursion branches out like a tree. For a 20x20 grid,
# you would perform over 130 billion calculations.
#
# The Fix: Before doing any math, we check a dictionary: if (i, j) in memo: return memo[(i, j)].
#
# If it’s not there, we calculate it once, store it, and never calculate it again.
#
# Step 5: The Final Result
# Once the recursion winds all the way back up to the starting cell (0, 0), it returns the final (max_total, min_total).
#
# We check if max_total is negative. If it is, the problem says we must return -1 (because we couldn't find a
# non-negative path).
#
# If it's positive, we apply the modulo: max_total % (10**9 + 7).
#

class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(i, j):
            # Base Case: Reached the bottom-right corner
            if i == m - 1 and j == n - 1:
                return grid[i][j], grid[i][j]

            # Check memo to see if we've already solved this cell
            if (i, j) in memo:
                return memo[(i, j)]

            res_max = float('-inf')
            res_min = float('inf')

            # Move Down
            if i + 1 < m:
                nxt_max, nxt_min = dp(i + 1, j)
                res_max = max(res_max, nxt_max * grid[i][j], nxt_min * grid[i][j])
                res_min = min(res_min, nxt_max * grid[i][j], nxt_min * grid[i][j])

            # Move Right
            if j + 1 < n:
                nxt_max, nxt_min = dp(i, j + 1)
                res_max = max(res_max, nxt_max * grid[i][j], nxt_min * grid[i][j])
                res_min = min(res_min, nxt_min * grid[i][j], nxt_max * grid[i][j])

            memo[(i, j)] = (res_max, res_min)
            return res_max, res_min

        # Start recursion from the top-left (0, 0)
        final_max, _ = dp(0, 0)

        # Return -1 if the maximum product is negative, else mod it
        return final_max % (10 ** 9 + 7) if final_max >= 0 else -1