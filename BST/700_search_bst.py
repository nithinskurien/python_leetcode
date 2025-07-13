from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.found = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.found = None
        def dfs(node: TreeNode):
            if not node:
                return
            if node.val == val:
                self.found = node
            if val < node.val:
                dfs(node.left)
            if val > node.val:
                dfs(node.right)
        dfs(root)
        return self.found
