# 110. Balanced Binary Tree
#
# Given a binary tree, determine if it is height-balanced.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#
# Input: root = []
# Output: true
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
#
# Logic:
# We can do a dfs where we will return 0 (height of tree) when we encounter a none (we want to set the child
# node without leafs to be set to one). We can then check the left and right heights and then compare the absolute
# difference between the heights and check if it is greater than one if yes then we return -1 to show that the result
# is a fail. If the difference is not greater than one then we will return the height to be the max of the left,
# right plus one.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            if left_height == -1:
                return -1
            right_height = dfs(root.right)
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return dfs(root) != -1
