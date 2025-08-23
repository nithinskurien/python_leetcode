# 57. Insert Interval
#
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
# start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an
# interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105
#
# Logic:
# We will iterate over the intervals till we see the interval that will result in the overlap. So till the new intervals
# start is greater than the existing intervals end, we will keep appending to the result. Then we have an overlap and
# we need to find the min and max of the interval we can do this till the end of the new interval is greater than or
# equal to the existing interval start. Once we resolve the start and end of the overlapping interval we can continue
# and add all the other intervals

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        index = 0
        start, end = newInterval[0], newInterval[1]
        while index < len(intervals) and start > intervals[index][1]:
            result.append(intervals[index])
            index += 1
        while index < len(intervals) and end >= intervals[index][0]:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1
        result.append([start, end])
        while index < len(intervals):
            result.append(intervals[index])
            index += 1
        return result