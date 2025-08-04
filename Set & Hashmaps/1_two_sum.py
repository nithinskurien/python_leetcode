# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
#
# Logic:
# We can store in hashmap the number as key and the index as value every time we encounter a number from the list,
# everytime we get a number from the list we can also check if a number that is target - number exists in the map
# if that number exists we can return the number and the index of the number which has the value target - number



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        hashmap = {}
        for index in range(len(nums)):
            targetBalance = hashmap.get(target - nums[index])
            if targetBalance is not None:
                return [targetBalance, index]
            hashmap[nums[index]] = index
        return output