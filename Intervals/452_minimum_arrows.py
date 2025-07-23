class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrow = 1
        arrowPos = points[0][1]
        for start, end in points:
            if start > arrowPos:
                arrow += 1
                arrowPos = end
        return arrow