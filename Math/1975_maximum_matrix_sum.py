# 1975. Maximum Matrix Sum
#
# You are given an n x n integer matrix. You can do the following operation any number of times:
#
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
#
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements
# using the operation mentioned above.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:
#
#
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105
#
# Logic:
# As we can use as many operations to choose 2 elements and multiply -1 to them, we can convert even number of negative
# numbers to positive. We can also change a greater negative number to a smaller one by shifting the sign by repeated
# multiplying by -1. So we just need to keep track of the total negative numbers including zero (as multiplying -1 to
# zero does not change the value). Add the absolute number to the sum and if the total negative number is even return
# the sum as we can change the negative number to positive. If the negative number count is odd then we just need to
# subtract the total sum by the smallest absolute value in the matrix. (twice that to be exact as we are adding the
# absolute value to the sum)


from cmath import inf


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        negative_nums = 0
        min_num = inf
        for row in range(rows):
            for col in range(cols):
                num = matrix[row][col]
                if num <= 0:
                    negative_nums += 1
                min_num = min(abs(num), min_num)
                res += abs(num)
        if negative_nums % 2 == 0:
            return res
        else:
            return res - (2 * min_num)
