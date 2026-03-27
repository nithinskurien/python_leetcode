# 2946. Matrix Similarity After Cyclic Shifts
#
#
# Logic:
# Non simulation method:
# Instead of modifying the matrix, the code checks:
#
# “If I shift this row by k, will every element still match its original position?”
#
# If any element doesn’t match → return False immediately.
#
# Simulation method:
# We run a simulation on the matrix and do the cyclic shifts

from copy import deepcopy


class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if row % 2 == 0:
                    if mat[row][col] != mat[row][(col + k) % cols]:
                        return False
                else:
                    if mat[row][col] != mat[row][(col - k) % cols]:
                        return False

        return True


class Solution2:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        mod_mat = deepcopy(mat)

        def shift(right, row):
            start, end = 0, len(row) - 1
            while start <= end:
                row[start], row[end] = row[end], row[start]
                if right:
                    start += 1
                else:
                    end -= 1

        for _ in range(k):
            for row in range(len(mat)):
                if row % 2 == 0:
                    shift(False, mat[row])
                else:
                    shift(True, mat[row])

        return mat == mod_mat

