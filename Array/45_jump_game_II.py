# 45. Jump Game II
#
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
# index i, you can jump to any index (i + j) where:
#
# 0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach index n - 1. The test cases are
# generated such that you can reach index n - 1.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4] Output: 2 Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index. Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
#
# Logic:
# Instead of trying all possible jumps (which would be slow), this code uses a greedy strategy:
#
# At every step, it keeps track of the farthest position you can reach.
# It only “commits” to a jump when it reaches the end of the current range.
#
# 🧠 Variables explained
# jumps = 0        # number of jumps made
# curr_step = 0    # end of current jump range
# max_step = 0     # farthest we can reach so far

# 🔁 Loop logic
# for i in range(len(nums) - 1):
# We stop at len(nums) - 1 because once we reach the last index, no more jumps are needed.
# 🚀 Step 1: Update farthest reachable position
# max_step = max(max_step, i + nums[i])
# From index i, you can go up to i + nums[i]
# Keep track of the farthest possible reach so far
#
# 🪜 Step 2: Decide when to jump
# if i >= curr_step:
#     jumps += 1
#     curr_step = max_step
# When you reach the end of the current jump range (curr_step), you must:
# Make a jump
# Extend your range to max_step
#
# 👉 Think of it like:
#
# You’re exploring all positions within the current jump
# Once you exhaust them, you “jump” to the best possible next range
#

class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        curr_step = 0
        max_step = 0

        for i in range(len(nums) - 1):
            max_step = max(max_step, i + nums[i])
            if i >= curr_step:
                jumps += 1
                curr_step = max_step

        return jumps