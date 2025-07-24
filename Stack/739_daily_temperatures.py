# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array
# answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If
# there is no future day for which this is possible, keep answer[i] == 0 instead.
#
# Example
# 1:
#
# Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Example
# 2:
#
# Input: temperatures = [30, 40, 50, 60]
# Output: [1, 1, 1, 0]
# Example
# 3:
#
# Input: temperatures = [30, 60, 90]
# Output: [1, 1, 0]
#
# Constraints:
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
#
# Explanation:
# The goal is to figure out, for each day, how many days you have to wait until a warmer temperature. To
# do this, the solution keeps track of the days that haven’t yet found a warmer day using a stack. As you go through
# each day: If the current day is warmer than any of the previous days in the stack, you now know how many days those
# earlier days had to wait. You record the number of days waited for each of them. Then, you add the current day to
# the stack, since it may need to wait for a warmer day too. In the end, days that never find a warmer temperature
# are left as zero. This approach efficiently processes the list in one pass.


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)
        for index in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                poppedIndex = stack.pop()
                result[poppedIndex] = index - poppedIndex
            stack.append(index)
        return result