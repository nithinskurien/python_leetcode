# 1536. Minimum Swaps to Arrange a Binary Grid
#
# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
#
# A grid is said to be valid if all the cells above the main diagonal are zeros.
#
# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
#
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
#
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# Example 3:
#
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1
#
# Logic:
# We can first calculate the count of trailing zeroes in an array. We need to find the row which will satisfy the count
# of the trailing zero. Once we find that row we need to swap the rows to bring it up. We can keep track of the swaps
# and repeat the steps till all the rows have their trailing zero row found. If we have not found the trailing zero row
# for any rows then we will hit the end (n) where we can return -1 to signify we cannot have the condition met.

class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Count trailing zeros for each row
        zeros = []
        for row in grid:
            count = 0
            for x in reversed(row):
                if x == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        swaps = 0

        for i in range(n):
            need = n - 1 - i
            j = i

            # Find a row that satisfies the requirement
            while j < n and zeros[j] < need:
                j += 1

            if j == n:
                return -1

            # Bring row up by swapping
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                swaps += 1
                j -= 1

        return swaps
