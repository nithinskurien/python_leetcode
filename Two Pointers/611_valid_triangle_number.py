# 611. Valid Triangle Number
#
# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
#
#
#
# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
# Logic: We can use the triangle inequality theorem which states that for the sides to make a valid triangle the sum
# of 2 sides should be greater that then the third side. i.e a + b > c, a + c > b, c + b > a. If we sort the numbers
# then we can simplify the search such that if a, b, c are the sorted numbers then we just need to check if a + b > c
# as c is bigger than a or b individually. As the numbers are sorted we can pin the last number and check the
# possible combinations by starting a left pointer at the start and a right pointer at one inder less than the end.
# We can then check if the sum of the left and right is greater than the value at the end if it is then we can add
# the count by right - left as if this combination is greater than the one between then will also be greater. If the
# sum is lesser than the value at index then we can reduce the left counter. We can continue this till the start of the
# array to return the count.

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        nums.sort()
        if n < 3:
            return 0
        for index in range(n - 1, 1, -1):
            left, right = 0, index - 1
            while left < right:
                if nums[left] + nums[right] > nums[index]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count