# 230. Kth Smallest Element in a BST
#
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
# values of the nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth
# smallest frequently, how would you optimize?
#
# Logic:
# The smallest node will mostly be on the left. We can recursively call the left and return if the left is None, or we
# have found the kth smallest value. When we return from the recursive call we can decrease k by one and check if
# the k value is zero if yes we can set the value of node to be returned to that node. If the left node is not the one
# we are looking for we can check the right.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ret = None
        self.k = None

    def recursive(self, root):
        if root is None or self.ret is not None:
            return
        self.recursive(root.left)
        self.k -= 1
        if self.k == 0:
            self.ret = root
        self.recursive(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ret = None
        self.recursive(root)
        return self.ret.val
