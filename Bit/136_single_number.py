class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for val in nums:
            result = result ^ val
        return result
