# 3567. Minimum Absolute Difference in Sliding Submatrix
#
# You are given an m x n integer matrix grid and an integer k.
#
# For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct
# values within that submatrix.
#
# Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the
# submatrix whose top-left corner is (i, j) in grid.
#
# Note: If all elements in the submatrix have the same value, the answer will be 0.
#
# A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and
# y1 <= y <= y2.
#
#
# Example 1:
#
# Input: grid = [[1,8],[3,-2]], k = 2
#
# Output: [[2]]
#
# Explanation:
#
# There is only one possible k x k submatrix: [[1, 8], [3, -2]].
# Distinct values in the submatrix are [1, 8, 3, -2].
# The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].
# Example 2:
#
# Input: grid = [[3,-1]], k = 1
#
# Output: [[0,0]]
#
# Explanation:
#
# Both k x k submatrix has only one distinct element.
# Thus, the answer is [[0, 0]].
# Example 3:
#
# Input: grid = [[1,-2,3],[2,3,5]], k = 2
#
# Output: [[1,2]]
#
# Explanation:
#
# There are two possible k × k submatrix:
# Starting at (0, 0): [[1, -2], [2, 3]].
# Distinct values in the submatrix are [1, -2, 2, 3].
# The minimum absolute difference in the submatrix is |1 - 2| = 1.
# Starting at (0, 1): [[-2, 3], [3, 5]].
# Distinct values in the submatrix are [-2, 3, 5].
# The minimum absolute difference in the submatrix is |3 - 5| = 2.
# Thus, the answer is [[1, 2]].
#
#
# Constraints:
#
# 1 <= m == grid.length <= 30
# 1 <= n == grid[i].length <= 30
# -105 <= grid[i][j] <= 105
# 1 <= k <= min(m, n)
#
# Logic:
# We can iterate over every sub-matrix of size k X k and check of the min diff by adding the num to a set and then
# sorting and finding the diff between the numbers. The min diff then can be added to the result matrix.

from cmath import inf


class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        res = [[0] * (m - k + 1) for _ in range(n - k + 1)]

        for i in range(n):
            for j in range(m):
                if i + k <= n and j + k <= m:
                    curr_set = set()
                    for ii in range(i, i + k):
                        for jj in range(j, j + k):
                            curr_set.add(grid[ii][jj])

                    if len(curr_set) == 1:
                        res[i][j] = 0

                    else:
                        min_diff = inf
                        sorted_num = sorted(curr_set)
                        for ii, v in enumerate(sorted_num):
                            if ii == 0:
                                continue
                            min_diff = min(min_diff, v - sorted_num[ii - 1])

                        res[i][j] = min_diff

        return res
