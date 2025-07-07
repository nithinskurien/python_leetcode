class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums_set_1 = set(nums1)
        nums_set_2 = set(nums2)
        diff_1 = nums_set_1 - nums_set_2
        diff_2 = nums_set_2 - nums_set_1
        output = [list(diff_1), list(diff_2)]
        return output
