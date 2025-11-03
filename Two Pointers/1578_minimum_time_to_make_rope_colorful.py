# 1578. Minimum Time to Make Rope Colorful
#
# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of
# the ith balloon.
#
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color,
# so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed
# integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from
# the rope.
#
# Return the minimum time Bob needs to make the rope colorful.
#
#
#
# Example 1:
#
#
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.
# Example 2:
#
#
# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
# Example 3:
#
#
# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
#
#
# Constraints:
#
# n == colors.length == neededTime.length
# 1 <= n <= 105
# 1 <= neededTime[i] <= 104
# colors contains only lowercase English letters.
#
# Logic:
# We can have 2 pointers one that goes through the colors and the second that starts from the first and goes till the
# color is not the same as the first. The idea is that if the color is the same we need to pop all the balloons that are
# the least time needed so if we find the max time we can just subtract that from the total. We can do this and return
# the total at the end after popping all balloons.

class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        i = 0
        res = 0
        while i < n:
            j = i
            total = 0
            max_sum = 0
            while j < n and colors[i] == colors[j]:
                total += neededTime[j]
                max_sum = max(max_sum, neededTime[j])
                j += 1
            res += total - max_sum
            i = j
        return res