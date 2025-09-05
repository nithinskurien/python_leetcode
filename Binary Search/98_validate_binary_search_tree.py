# 98. Validate Binary Search Tree
#
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
#
# Logic:
# For a binary search tree the left node and all the children should be less than the root node and the right and all
# the children should be greater than the root node. Initially the root node has no upper or lower bounds, as the tree
# goes down each level the bounds get tighter and tighter. We will check this recursively


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursive(self, root: Optional[TreeNode], leftBound: float, rightBound: float) -> bool:
        if root is None:
            return True
        elif not (leftBound < root.val < rightBound):
            return False
        else:
            return self.recursive(root.left, leftBound, root.val) and self.recursive(root.right, root.val, rightBound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root, float('-inf'), float('inf'))
