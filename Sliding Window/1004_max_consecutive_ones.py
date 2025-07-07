class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left_pointer, right_pointer, max_ones = 0, 0, 0
        while right_pointer < len(nums):
            if nums[right_pointer] == 0:
                k -= 1
            while k < 0:
                if nums[left_pointer] == 0:
                    k += 1
                left_pointer += 1
            right_pointer += 1
            max_ones = max(max_ones, right_pointer - left_pointer)
        return max_ones


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
