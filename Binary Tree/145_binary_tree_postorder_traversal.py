# 145. Binary Tree Postorder Traversal
#
# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
#
#
# Example 1:
#
# Input: root = [1,null,2,3]
#
# Output: [3,2,1]
#
# Explanation:
#
#
#
# Example 2:
#
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
#
# Output: [4,6,7,5,2,9,8,3,1]
#
# Explanation:
#
#
#
# Example 3:
#
# Input: root = []
#
# Output: []
#
# Example 4:
#
# Input: root = [1]
#
# Output: [1]
#
#
#
# Constraints:
#
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
# Logic:
# We can iteratively call a function to traverse the tree but append the val after going left and right.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res
