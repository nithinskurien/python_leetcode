class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left_pointer, right_pointer, pairs = 0, len(nums) - 1, 0
        nums.sort()
        while left_pointer < right_pointer:
            sum = nums[left_pointer] + nums[right_pointer]
            if sum < k:
                left_pointer += 1
            elif sum > k:
                right_pointer -= 1
            else:
                pairs += 1
                left_pointer += 1
                right_pointer -= 1
        return pairs