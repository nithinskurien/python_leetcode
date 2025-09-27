# 812. Largest Triangle Area
#
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest
# triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
#
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:
#
# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
#
#
# Constraints:
#
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
#
# Logic:
# We can use the shoelace triangle area formula where area of a triangle with 3 point A, B & C is
# 0.5 * abs(A[x] * (B[y] - C[y]) + B[x] * (C[y] - A[y]) + C[x] * (A[y] - B[y])). We can then use combinations package
# to get all the possible combinations of 3 points and iterate over it till we get the max area.


from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        def area(A, B, C) -> float:
            return 0.5 * abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))

        combs = combinations(points, 3)
        maxArea = 0

        for comb in combs:
            maxArea = max(maxArea, area(comb[0], comb[1], comb[2]))
        return maxArea
