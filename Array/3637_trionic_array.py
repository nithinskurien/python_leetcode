# 3637. Trionic Array I
#
# You are given an integer array nums of length n.
#
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#
# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,4,2,6]
#
# Output: true
#
# Explanation:
#
# Pick p = 2, q = 4:
#
# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).
# Example 2:
#
# Input: nums = [2,1,3]
#
# Output: false
#
# Explanation:
#
# There is no way to pick p and q to form the required three segments.
#
#
#
# Constraints:
#
# 3 <= n <= 100
# -1000 <= nums[i] <= 1000
#
# Logic:
# We want to keep track of how many times the array will change direction. In the trionic array the switch should happen
# twice after strictly increasing. We can initialise a variable called increasing to be the result of nums[1] greater
# than nums[0] if this is false we can already return False as the first period is decreasing not increasing. Now we
# just have to keep track of how many times the array switches from increasing to decreasing and decreasing to
# increasing. If the number of switch is not 2 we return False else return True.

class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        increasing = nums[1] > nums[0]
        switch = 0
        if not increasing:
            return False
        for index in range(2, len(nums)):
            if nums[index] > nums[index - 1]:
                if not increasing:
                    increasing = True
                    switch += 1
            elif nums[index] < nums[index - 1]:
                if increasing:
                    increasing = False
                    switch += 1
            else:
                return False
        return switch == 2

