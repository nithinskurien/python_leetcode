class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left_pointer, right_pointer = 0, 0
        while right_pointer < len(nums):
            if nums[right_pointer] != 0:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
            right_pointer += 1
        print(nums)



if __name__ == "__main__":
    solution = Solution()
    solution.moveZeroes([4,2,4,0,0,3,0,5,1,0])
