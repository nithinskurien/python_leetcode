# 756. Pyramid Transition Matrix
#
# You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each
# row of blocks contains one less block than the row beneath it and is centered on top.
#
# To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A
# triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of
# three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom
# blocks respectively, and the third character is the top block.
#
# For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right)
# block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom. You
# start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.
#
# Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every
# triangular pattern in the pyramid is in allowed, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# Output: true
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
# There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
# Example 2:
#
#
# Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"] Output: false Explanation: The allowed triangular
# patterns are shown on the right. Starting from the bottom (level 4), there are multiple ways to build level 3,
# but trying all the possibilites, you will get always stuck before building level 1.
#
#
# Constraints:
#
# 2 <= bottom.length <= 6
# 0 <= allowed.length <= 216
# allowed[i].length == 3
# The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
# All the values of allowed are unique.
#
# Logic:
# Start with a bottom row (e.g. "ABC").
#
# Each adjacent pair ("AB", "BC") can produce certain characters above them.
#
# You try all possible combinations recursively until:
#
# You reach a row of length 1 → success ✅
#
# You exhaust all possibilities → failure ❌
#
# This is a DFS + backtracking problem with memoization to prune repeated work.
# 1. Preprocessing the allowed transitions
# map = defaultdict(list)
#
# for left, right, top in allowed:
#     map[left + right].append(top)
#
#
# We convert:
#
# ["ABC", "ABD", "BCE"]
#
#
# into:
#
# {
#   "AB": ["C", "D"],
#   "BC": ["E"]
# }
#
#
# So later, when we see "AB" in the bottom row, we know which characters can go on top.
#
# 2. The recursive backtracking function
# def backtrack(bottom, row, i):
#
#
# Parameters:
#
# Variable	Meaning
# bottom	Current level we are building from
# row	The next row being built
# i	Current index in bottom
# 3. Base cases
# ✅ Success case
# if n == 1:
#     return True
#
#
# If the current row has length 1, we successfully built the pyramid.
#
# 🛑 Finished building one row
# if n == i:
#     if row in seen:
#         return False
#     seen.add(row)
#     return backtrack(row, "", 1)
#
#
# If we've processed all adjacent pairs in bottom, we:
#
# Check if we’ve already tried this row before (seen) → prune duplicates
#
# Recurse upward with the new row
#
# 4. Try all possible transitions
# pair = bottom[i - 1] + bottom[i]
# for curr in map[pair]:
#     if backtrack(bottom, row + curr, i + 1):
#         return True
# return False
#
#
# For each adjacent pair:
#
# Look up possible top characters
#
# Try each one
#
# If any path leads to success → return True
#
# 5. Start recursion
# return backtrack(bottom, "", 1)
#
#
# Start building the next row from index 1.

from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        n = len(bottom)
        map = defaultdict(list)
        seen = set()

        for left, right, top in allowed:
            map[left + right].append(top)

        def backtrack(bottom, row, i):
            n = len(bottom)
            if n == 1:
                return True
            if n == i:
                if row in seen:
                    return False
                seen.add(row)
                return backtrack(row, "", 1)
            pair = bottom[i - 1] + bottom[i]
            for curr in map[pair]:
                if backtrack(bottom, row + curr, i + 1):
                    return True
            return False

        return backtrack(bottom, "", 1)
