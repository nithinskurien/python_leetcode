# 48. Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
# another 2D matrix and do the rotation.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
# Logic:
# To rotate the matrix clockwise we need to first transpose the matrix and once that is done we just need to reverse the
# columns and that will result in the rotated matrix

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for row in range(size):
            for col in range(row + 1, size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(size):
            matrix[row].reverse()