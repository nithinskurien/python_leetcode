# 1382. Balance a Binary Search Tree
#
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is
# more than one answer, return any of them.
#
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,1,3]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105
#
# Logic:
# We can first iterate inorder to get the node values. Then we can recursively find the mid-point of the array and build
# the BST by assigning the middle of the first and second mid-points of arrays to left and right till left is greater
# than right

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        inorder(root)

        def bst(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            node = TreeNode(nodes[mid])
            node.left = bst(left, mid - 1)
            node.right = bst(mid + 1, right)
            return node

        return bst(0, len(nodes) - 1)