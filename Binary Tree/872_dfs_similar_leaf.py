from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs_tree1 = self.findleafs(root1)
        leafs_tree2 = self.findleafs(root2)
        return leafs_tree1 == leafs_tree2

    def findleafs(self, root: Optional[TreeNode]) -> str:
        leafs = ""
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node:
                if curr_node.left is None and curr_node.right is None:
                    leafs += '[' + str(curr_node.val) + ']'
                stack.append(curr_node.left)
                stack.append(curr_node.right)
        return leafs
