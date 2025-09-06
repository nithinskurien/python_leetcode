# 226. Invert Binary Tree
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
# Logic:
# We can recursively go to each node and switch the left and right, we will return from the recursive call when a node
# is None meaning there are no children left


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursive(self, root: Optional[TreeNode]):
        if root is None:
            return
        root.right, root.left = root.left, root.right
        self.recursive(root.left)
        self.recursive(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursive(root)
        return root
