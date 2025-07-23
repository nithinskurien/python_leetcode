class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prevEnd = intervals[0][1]
        overlap = 0
        for start, end in intervals[1:]:
            if start < prevEnd:
                overlap += 1
            else:
                prevEnd = end
        return overlap
