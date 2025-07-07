import sys


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        smallest_first_num = sys.maxsize
        smallest_second_num = sys.maxsize
        for index in range(len(nums)):
            if smallest_first_num >= nums[index]:
                smallest_first_num = nums[index]
            elif smallest_second_num >= nums[index]:
                smallest_second_num = nums[index]
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingTriplet([1,2,1,3]))
