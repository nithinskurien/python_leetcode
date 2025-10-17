# 40. Combination Sum II
#
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
# candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
# Constraints:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
# Logic:
# We will recursively add candidates to the curr array and append it to the result when the target becomes zero. We only
# need the first candidate of a number to avoid duplicates, so we will have a check to see if the index is greater than
# start and the previous candidate is the same if so we will just continue the loop.

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def comb(curr, start, target):
            if target == 0:
                result.append(curr)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                comb(curr + [candidates[i]], i + 1, target - candidates[i])

        comb([], 0, target)
        return result
