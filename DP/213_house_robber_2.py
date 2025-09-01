# 213. House Robber II
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
# two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#
# Logic: The question is similar to the house robber 1 where we cannot rob adjacent houses in a line. So we will
# accumulate the max money we can make at a house based on if we will rob the current house or not. So if we are at
# house 1 we will set the max money based on whether we would rob the current or previous house. For all other houses
# we will check if the cumulative sum of robbing the current house with the sum of house 2 index back is bigger then
# robbing the previous house and so on. For the circular case we will split the input array such that one array does
# not have the start, while the second does not have the end. We can the check what is the max of both arrays passed to
# the house rob 1 algorithm.

class Solution:
    def houseRob1(self, nums: list[int]) -> int:
        for index in range(1, len(nums)):
            if index == 1:
                nums[index] = max(nums[index], nums[0])
            else:
                nums[index] = max(nums[index] + nums[index - 2], nums[index - 1])
        return nums[-1]

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        else:
            return max(self.houseRob1(nums[1:]), self.houseRob1(nums[:-1]))