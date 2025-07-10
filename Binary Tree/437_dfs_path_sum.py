from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pathSumDict = defaultdict(int)
        self.pathCount = None

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pathSumDict = defaultdict(int)
        self.pathSumDict[0] = 1
        self.pathCount = 0

        def dfs(node: TreeNode, currSum: int):
            if node is None:
                return
            currSum += node.val
            self.pathCount += self.pathSumDict[currSum - targetSum]
            self.pathSumDict[currSum] += 1
            if node.left:
                dfs(node.left, currSum)
            if node.right:
                dfs(node.right, currSum)
            self.pathSumDict[currSum] -= 1
        dfs(root, 0)
        return self.pathCount
