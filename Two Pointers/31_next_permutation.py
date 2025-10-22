# 31. Next Permutation
#
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3,
# 1], [3,1,2], [3,2,1]. The next permutation of an array of integers is the next lexicographically greater
# permutation of its integer. More formally, if all the permutations of the array are sorted in one container
# according to their lexicographical order, then the next permutation of that array is the permutation that follows
# it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest
# possible order (i.e., sorted in ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2]. Similarly, the next permutation of arr = [2,3,
# 1] is [3,1,2]. While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a
# lexicographical larger rearrangement. Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
# Logic:
# We will need to first iterate from the end of the list to get the first index where the number is decreasing. If we
# have not found any index and have reached zero we can just reverse the list to get the next as we have the biggest
# number and can get the smallest by reversing. Once we have identified the number we need to switch we need to find
# the second number we need to switch with for this we can iterate from the back till we reach a value that is larger
# than the first index, and then we swap the values and reverse the rest of the string.
# e.g. [1, 3, 4, 2] -> we find that switch_large = 2 (the actual index is switch_large - 1, we will account for this
# later). We need to find what do we switch with for which the second index should be greater than first so we get
# switch small = 2, as stated before we switch switch_large - 1 and switch_small so [1, 3, 4, 2] -> [1, 4, 3, 2]
# now we just reverse the list from switch_large i.e [1, 4, 2, 3]


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        switch_large = len(nums) - 1
        switch_small = len(nums) - 1

        while switch_large > 0 and nums[switch_large - 1] >= nums[switch_large]:
            switch_large -= 1

        if switch_large == 0:
            nums.reverse()
            return

        while switch_small >= switch_large and nums[switch_small] <= nums[switch_large - 1]:
            switch_small -= 1

        nums[switch_large - 1], nums[switch_small] = nums[switch_small], nums[switch_large - 1]

        nums[switch_large:] = reversed(nums[switch_large:])
        print(nums)

if __name__=="__main__":
    print(Solution().nextPermutation([1, 3, 4, 2]))
