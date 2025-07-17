class Solution:
    def rob(self, nums: list[int]) -> int:
        for house in range(1, len(nums)):
            if house == 1:
                nums[house] = max(nums[house], nums[house - 1])
            else:
                nums[house] = max(nums[house - 1], nums[house] + nums[house - 2])
        return nums[-1]