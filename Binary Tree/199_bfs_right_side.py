from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        nodes = deque([root])
        solu = []
        if not root:
            return []
        while nodes:
            solu.append(nodes[-1].val)
            level_length = len(nodes)
            for index in range(level_length):
                curr_node = nodes.popleft()
                if curr_node.left:
                    nodes.append(curr_node.left)
                if curr_node.right:
                    nodes.append(curr_node.right)
        return solu
