# 1886. Determine Whether Matrix Can Be Obtained By Rotation
#
# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by
# rotating mat in 90-degree increments, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
# Example 2:
#
#
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.
# Example 3:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
#
#
# Constraints:
#
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] and target[i][j] are either 0 or 1.
#
# Logic:
# We can rotate a matrix by first flipping the rows and then swapping the diagonal elements. So we can do this upto a
# max of 4 times and compare if the rotated matrix is equal to the target.

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)

        def rotate():
            for row in range(n // 2):
                for col in range(n):
                    mat[row][col], mat[n - 1 - row][col] = mat[n - 1 - row][col], mat[row][col]

            for row in range(n):
                for col in range(row + 1):
                    mat[row][col], mat[col][row] = mat[col][row], mat[row][col]

            return mat == target

        for i in range(4):
            if rotate():
                return True

        return False
