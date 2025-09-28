# 976. Largest Perimeter Triangle
#
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of
# these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
#
#
#
# Example 1:
#
# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:
#
# Input: nums = [1,2,1,10]
# Output: 0
# Explanation:
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106
#
# Logic:
# We can use the triangle inequality theorem which states that for the sides to make a valid triangle the sum
# of 2 sides should be greater that then the third side. i.e a + b > c, a + c > b, c + b > a. If we sort the numbers
# then we can simplify the search such that if a, b, c are the sorted numbers then we just need to check if a + b > c
# as c is bigger than a or b individually. We now just need to get the largest numbers of the array and see if a valid
# triangle can be made if not we will try with the next top 3 numbers and so on. Once we are able to make a valid
# triangle we can return the value. We can do this by sorting and iterating over an array or using a heap to get the
# largest numbers.


import heapq


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        for index in range(n - 1, 1, -1):
            if nums[index] < nums[index - 1] + nums[index - 2]:
                return nums[index] + nums[index - 1] + nums[index - 2]
        return 0


class Solution2:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while len(nums) >= 3:
            a = -heapq.heappop(nums)
            b = -heapq.heappop(nums)
            c = -nums[0]

            if b + c > a:
                return a + b + c

            heapq.heappush(nums, -b)

        return 0


if __name__ == "__main__":
    print(Solution().largestPerimeter([2, 1, 2]))
