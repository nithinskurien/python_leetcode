class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        prefix = 1
        for index in range(len(nums)):
            answer[index] *= prefix
            prefix = prefix * nums[index]
        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            answer[index] *= postfix
            postfix = postfix * nums[index]
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
