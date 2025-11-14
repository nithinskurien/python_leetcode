# 2536. Increment Submatrices by One
#
# You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled
# with zeroes.
#
# You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the
# following operation:
#
# Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i,
# col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i. Return the matrix mat
# after performing every query.
#
#
#
# Example 1:
#
#
# Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]] Output: [[1,1,0],[1,2,1],[0,1,1]] Explanation: The diagram above
# shows the initial matrix, the matrix after the first query, and the matrix after the second query. - In the first
# query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2,
# 2). - In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom
# right corner (1, 1). Example 2:
#
#
# Input: n = 2, queries = [[0,0,1,1]]
# Output: [[1,1],[1,1]]
# Explanation: The diagram above shows the initial matrix and the matrix after the first query.
# - In the first query we add 1 to every element in the matrix.
#
# Logic:
#
# diff_mat marks where each +1 effect starts and ends
# (so you don’t have to update every cell in every query).
#
# Then the double loop turns those markers into real values by computing the full 2D prefix sum, cell by cell.
#
# The formula adds:
#
# what was added above,
#
# what was added to the left,
#
# what was added here,
#
# minus the double-counted diagonal.
#
# The result in mat is the final matrix after all the +1 rectangle additions.


class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]
        diff_mat = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff_mat[r1][c1] += 1  # start effect
            diff_mat[r2 + 1][c1] -= 1  # end effect row
            diff_mat[r1][c2 + 1] -= 1  # end effect col
            diff_mat[r2 + 1][c2 + 1] += 1  # cancel effect of both ends

        for row in range(n):
            for col in range(n):
                acc_col = mat[row - 1][col] if row > 0 else 0
                acc_row = mat[row][col - 1] if col > 0 else 0
                acc_diag = mat[row - 1][col - 1] if row > 0 and col > 0 else 0
                mat[row][col] = diff_mat[row][col] + acc_col + acc_row - acc_diag

        return mat