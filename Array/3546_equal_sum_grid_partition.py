# 3546. Equal Sum Grid Partition I
#
# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either
# one horizontal or one vertical cut on the grid such that:
#
# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.
#
#
#
# Example 1:
#
# Input: grid = [[1,4],[2,3]]
#
# Output: true
#
# Explanation:
#
#
#
# A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer
# is true.
#
# Example 2:
#
# Input: grid = [[1,3],[2,4]]
#
# Output: false
#
# Explanation:
#
# No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.
#
#
#
# Constraints:
#
# 1 <= m == grid.length <= 105
# 1 <= n == grid[i].length <= 105
# 2 <= m * n <= 105
# 1 <= grid[i][j] <= 105
#
# Logic:
# We can first find the total, check if the total is not odd if it is we can return false as an odd total
# cannot be split equally. We can then iterate over the rows and columns summing up the individual elements. We can
# then check if the twice that amount is equal to the total if yes we can return true. If we have checked all the rows
# and cols and not yet returned true we can return false.

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                total += grid[i][j]

        if total % 2 == 1:
            return False

        temp = 0
        for i in range(m):
            temp += sum(grid[i])
            if total == 2 * temp:
                return True

        temp = 0
        for j in range(n):
            for i in range(m):
                temp += grid[i][j]
            if total == 2 * temp:
                return True

        return False
