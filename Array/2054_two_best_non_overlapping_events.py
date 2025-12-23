# 2054. Two Best Non-Overlapping Events
#
# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith
# event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei.
# You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.
#
# Return this maximum sum.
#
# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts
# and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must
# start at or after t + 1.
#
#
#
# Example 1:
#
#
# Input: events = [[1,3,2],[4,5,2],[2,4,3]]
# Output: 4
# Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
# Example 2:
#
# Example 1 Diagram
# Input: events = [[1,3,2],[4,5,2],[1,5,5]]
# Output: 5
# Explanation: Choose event 2 for a sum of 5.
# Example 3:
#
#
# Input: events = [[1,5,3],[1,5,1],[6,6,5]]
# Output: 8
# Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
#
#
# Constraints:
#
# 2 <= events.length <= 105
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 109
# 1 <= valuei <= 106
#
# Logic:
# We can have 2 sorted array based on the start and end interval time. For every index in starts we are trying to find a
# value in the sorted ends that would give the maximum sum. We can do this for every value in the events and return the
# result.

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        starts = sorted(events)
        ends = sorted(events, key=lambda x: x[1])
        i = 0
        best_before = 0
        result = 0
        for start, end, value in starts:
            while ends[i][1] < start:
                best_before = max(best_before, ends[i][2])
                i += 1
            result = max(result, best_before + value)
        return result