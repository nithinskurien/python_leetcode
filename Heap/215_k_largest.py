import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        return nums[len(nums) - k + 1]
