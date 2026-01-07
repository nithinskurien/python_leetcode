# 1339. Maximum Product of Splitted Binary Tree
#
# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product
# of the sums of the subtrees is maximized.
#
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109
# + 7.
#
# Note that you need to maximize the answer before taking the mod and not after taking it.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:
#
#
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104
#
# Logic:
# We can make use of the fact that to find the sum of a splitted subtree we just need to find the sum of one of them as
# we can just subtract the sum of the first from the total sum of the tree. So we can iterate over the tree to find the
# total sum and do a second pass to compute the product and store the maximum.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0

        def getSum(node):
            if not node:
                return 0
            left_sum = getSum(node.left)
            right_sum = getSum(node.right)
            return left_sum + right_sum + node.val

        def dfs_nodes(node):
            if not node:
                return 0
            left_sum = dfs_nodes(node.left)
            right_sum = dfs_nodes(node.right)
            self.res = max(self.res, left_sum * (total - left_sum), right_sum * (total - right_sum))
            return left_sum + right_sum + node.val

        total = getSum(root)
        dfs_nodes(root)

        return self.res % (10 ** 9 + 7)
