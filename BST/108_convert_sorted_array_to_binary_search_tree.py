# 108. Convert Sorted Array to Binary Search Tree
#
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
# binary search tree.
#
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
#
# Logic:
# We can recursively build nodes where the root is the middle of left and right indices of the nums array and
# recursively build out the tree.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def build_node(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(nums[mid],
                            build_node(left, mid - 1),
                            build_node(mid + 1, right))

        return build_node(0, len(nums) - 1)
