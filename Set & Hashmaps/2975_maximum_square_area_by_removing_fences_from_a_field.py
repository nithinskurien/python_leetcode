# 2975. Maximum Square Area by Removing Fences From a Field
#
# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal
# and vertical fences given in arrays hFences and vFences respectively.
#
# Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the
# coordinates (1, vFences[i]) to (m, vFences[i]).
#
# Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is
# impossible to make a square field.
#
# Since the answer may be large, return it modulo 109 + 7.
#
# Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m,
# n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.
#
#
#
# Example 1:
#
#
#
# Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
# Output: 4
# Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
# Example 2:
#
#
#
# Input: m = 6, n = 7, hFences = [2], vFences = [4]
# Output: -1
# Explanation: It can be proved that there is no way to create a square field by removing fences.
#
#
# Constraints:
#
# 3 <= m, n <= 109
# 1 <= hFences.length, vFences.length <= 600
# 1 < hFences[i] < m
# 1 < vFences[i] < n
# hFences and vFences are unique.
#
# Logic:
# We can iterate over the vertical & horizontal fences and see what is the gap widths we can create and store them in a
# set. We can then get the max common width from both the sides and return that as the area.

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        hFences += [1, m]
        vFences += [1, n]
        hFences.sort()
        vFences.sort()
        hSet, vSet = set(), set()
        res = -1

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hSet.add(hFences[j] - hFences[i])

        for i in range(len(vFences)):
            for j in range(len(vFences) - 1, i, -1):
                width = vFences[j] - vFences[i]
                if width in hSet:
                    res = max(res, width * width)
                    break

        return res % (10 ** 9 + 7) if res >= 0 else -1
