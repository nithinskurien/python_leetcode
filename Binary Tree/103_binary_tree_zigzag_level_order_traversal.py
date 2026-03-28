# 103. Binary Tree Zigzag Level Order Traversal
#
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
# right, then right to left for the next level and alternate between).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
# Logic:
# We can use a queue and do a bfs to get all the nodes in each level. At each iteration we go through all the nodes in a
# level and add the new children. We initialise an array and collect the nodes and then check if it is an odd or even
# level and then either keep the order or reverse the order of the level_array before adding it to the result. After
# iterating over all the levels we return the result.

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque([root])
        move_left = False
        res = []
        if not root:
            return res
        while queue:
            level_len = len(queue)
            curr_level = []
            for _ in range(level_len):
                current_node = queue.popleft()
                curr_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            if move_left:
                curr_level.reverse()

            res.append(curr_level)
            move_left = not move_left

        return res


