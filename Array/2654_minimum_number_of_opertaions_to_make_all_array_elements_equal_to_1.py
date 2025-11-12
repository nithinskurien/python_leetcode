# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
#
# You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the
# array any number of times:
#
# Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
# Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.
#
# The gcd of two integers is the greatest common divisor of the two integers.
#
#
#
# Example 1:
#
# Input: nums = [2,6,3,4]
# Output: 4
# Explanation: We can do the following operations:
# - Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
# - Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
# - Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
# - Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
# Example 2:
#
# Input: nums = [2,10,6,14]
# Output: -1
# Explanation: It can be shown that it is impossible to make all the elements equal to 1.
#
#
# Constraints:
#
# 2 <= nums.length <= 50
# 1 <= nums[i] <= 106
#
# Logic:
# There are 3 situations that would influence the solution. a) there is a one in the array then we just need len(nums)
# - ones operations. b) We are not able to get the gcd of any numbers to come to one which means we will return -1.
# c) We will have a subset of numbers whose gcd would give us one, and we can use that one to change the rest to ones
# for e.g [6, 10, 15] here the gcd of 6, 10 is 2 of 10, 15 is 5 but for [6, 10, 15] we can get 1 so the minimum length
# of subarray is 3. If we cannot find the minimum length of subarray then return -1 as we are not able to make a one.

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        one_count = 0

        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        for num in nums:
            if num == 1:
                one_count += 1

        min_sub_array_len = float("inf")
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i, len(nums)):
                if j - i + 1 >= min_sub_array_len:
                    break
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_sub_array_len = min(min_sub_array_len, j - i + 1)
                    break

        if min_sub_array_len == float("inf"):
            return -1
        if one_count > 0:
            return len(nums) - one_count
        else:
            return (min_sub_array_len - 1) + len(nums) - 1


if __name__ == "__main__":
    print(Solution().minOperations([2, 10, 6, 1]))
