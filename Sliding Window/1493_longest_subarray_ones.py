class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left_pointer, right_pointer, zero_count, max_count = 0, 0, 1, 0
        while right_pointer < len(nums):
            if nums[right_pointer] == 0:
                zero_count -= 1
                while zero_count < 0:
                    if nums[left_pointer] == 0:
                        zero_count += 1
                    left_pointer += 1
            right_pointer += 1
            max_count = max(max_count, right_pointer - left_pointer)
        return max_count - 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))