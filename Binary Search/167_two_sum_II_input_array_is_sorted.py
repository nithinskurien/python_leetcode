# 167. Two Sum II - Input Array Is Sorted
#
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
# that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1
# <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1,
# index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#
#
# Constraints:
#
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
#
# Logic:
# We can initialise 2 pointers left and right and then until left is greater than right keep adding the numbers and the
# index left and right if they are equal we can return the list of left and right. If the sum is greater than target we
# can reduce the right, if the sum is lesser than the target we can increase the left.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_num = numbers[left] + numbers[right]
            if sum_num == target:
                return [left + 1, right + 1]
            elif sum_num > target:
                right -= 1
            else:
                left += 1

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)

        def binary_search(pos, sum_target):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == sum_target:
                    if mid != pos:
                        return mid
                    left = mid + 1
                elif numbers[mid] < sum_target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        for index in range(n):
            sol = binary_search(index, (target - numbers[index]))
            if sol != -1:
                return [index + 1, sol + 1]


if __name__ == '__main__':
    print(Solution().twoSum([5, 25, 75], 100))
