class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for index in range(len(nums)):
            right_sum -= nums[index]
            if left_sum == right_sum:
                return index
            left_sum += nums[index]
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex([1,7,3,6,5,6]))
