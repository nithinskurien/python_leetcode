# 54. Spiral Matrix
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
# Logic:
# We will traverse the matrix in a spiral fashion shrinking the bounds of the matrix with every step. We will move right
# and once we reach the rightmost we will reduce the min row, we will then move down and reduce the max col, we will
# then move to the left and then reduce the max row and finally move up and reduce the min col. We will loop through the
# same steps till the min row and max row is the same and min col and max col is the same.


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        minRow, maxRow, minCol, maxCol = 0, len(matrix), 0, len(matrix[0])
        row = 0
        output = []

        while minRow < maxRow and minCol < maxCol:
            for col in range(minCol, maxCol):
                output.append(matrix[minRow][col])
            minRow += 1

            for row in range(minRow, maxRow):
                output.append(matrix[row][col])
            maxCol -= 1

            if minRow < maxRow and minCol < maxCol:
                for col in range(maxCol - 1, minCol - 1, -1):
                    output.append(matrix[row][col])
                maxRow -= 1

                for row in range(maxRow - 1, minRow - 1, -1):
                    output.append(matrix[row][col])
                minCol += 1

        return output


if __name__ == "__main__":
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
