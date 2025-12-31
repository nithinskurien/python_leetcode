# 101. Symmetric Tree
#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
# Follow up: Could you solve it both recursively and iteratively?
#
# Logic:
# We can call a recursive function that would check if the symmetric nodes are equal (e.g. right of a left child and
# left of a right child, or the left of a left child and the right of a right child). We can have the success case to
# return true when both the nodes are equal and the false when the values of the nodes are not equal.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return check(left.right, right.left) and check(left.left, right.right)

        return check(root.left, root.right)
