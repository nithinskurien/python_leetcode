# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than
# or equal to threshold or return 0 if there is no such square.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:
#
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105
#
# Logic:
# We can pre-compute the 2D prefix matrix and then go through every index and grow a square size and check if the square
# sum is less than threshold if not we can break the iteration as if the current size is more than threshold the next
# larger size will also have the size larger (there are not negative numbers). 

class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        ps = [[0] * m for _ in range(n)]
        res = 0

        for i in range(n):
            for j in range(m):
                ps[i][j] = (mat[i][j]
                            + (ps[i - 1][j] if i > 0 else 0)
                            + (ps[i][j - 1] if j > 0 else 0)
                            - (ps[i - 1][j - 1] if i > 0 and j > 0 else 0))

        def mat_sum(row, col, size):
            return (ps[row + size][col + size]
                    - (ps[row - 1][col + size] if row > 0 and col + size < m else 0)
                    - (ps[row + size][col - 1] if col > 0 and row + size < n else 0)
                    + (ps[row - 1][col - 1] if row > 0 and col > 0 else 0))

        for row in range(n):
            for col in range(m):
                for size in range(min(n - row, m - col)):
                    curr = mat_sum(row, col, size)
                    if curr <= threshold:
                        res = max(res, size + 1)
                    else:
                        break

        return res