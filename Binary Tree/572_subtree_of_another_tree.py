# 572. Subtree of Another Tree
#
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants. The
# tree could also be considered as a subtree of itself.
#
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104
#
# Logic 1:
# We can stringify the Tree and subtree and then check if the subtree is a substring of the tree
#
# Logic 2:
# We can recursively check if the subtree of a tree is equal to the subroot, we can use a recursive equal function to
# check if 2 trees are equal. We can then check if the subroot is equal to the subtree from all the nodes.
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ser(n):
            if not n:
                return "$#"
            return "$" + str(n.val) + ser(n.left) + ser(n.right)

        return ser(subRoot) in ser(root)


class Solution2:
    def isSametree(self, rootA: Optional[TreeNode], rootB: Optional[TreeNode]) -> bool:
        if rootA is None and rootB is None:
            return True
        if rootA is None or rootB is None or rootA.val != rootB.val:
            return False
        return self.isSametree(rootA.left, rootB.left) and self.isSametree(rootA.right, rootB.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
