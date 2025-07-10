import sys
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        current_level = 1
        min_level = 1
        max_sum = -sys.maxsize
        if not root:
            return 0
        while queue:
            level_length = len(queue)
            current_sum = 0
            for index in range(level_length):
                current_node = queue.popleft()
                current_sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            if current_sum > max_sum:
                min_level = current_level
                max_sum = current_sum
            current_level += 1
        return min_level
