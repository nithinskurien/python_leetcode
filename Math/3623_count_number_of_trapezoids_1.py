# 3623. Count Number of Trapezoids I
#
# You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on
# the Cartesian plane.
#
# A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the
# x-axis). Two lines are parallel if and only if they have the same slope.
#
# Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.
#
# Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
#
# Output: 3
#
# Explanation:
#
#
#
# There are three distinct ways to pick four points that form a horizontal trapezoid:
#
# Using points [1,0], [2,0], [3,2], and [2,2].
# Using points [2,0], [3,0], [3,2], and [2,2].
# Using points [1,0], [3,0], [3,2], and [2,2].
# Example 2:
#
# Input: points = [[0,0],[1,0],[0,1],[2,1]]
#
# Output: 1
#
# Explanation:
#
#
#
# There is only one horizontal trapezoid that can be formed.
#
#
#
# Constraints:
#
# 4 <= points.length <= 105
# –108 <= xi, yi <= 108
# All points are pairwise distinct.
#
# Logic:
# We can first create a map of points at a y level. As these points will be used to create sides. The number of sides
# that can be made of points will be comb(x, 2). This value can then be added to an accumulated value which can be used
# to multiply with the current value to give the total trapezoid possible.


from collections import defaultdict
from math import comb


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        MOD = 10**9 + 7
        levels = defaultdict(int)
        for x, y in points:
            levels[y] += 1
        res = 0
        accumulated = 0
        for v in levels.values():
            curr = comb(v, 2)
            res = (res + curr * accumulated) % MOD
            accumulated = (accumulated + curr) % MOD
        return res