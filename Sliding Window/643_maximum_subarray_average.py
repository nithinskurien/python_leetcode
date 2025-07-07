class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        for index in range(len(nums) - k):
            curr_sum += nums[index + k] - nums[index]
            max_sum = max(curr_sum, max_sum)
        return max_sum/k


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
