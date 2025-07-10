from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = None

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node: TreeNode, isLeft: bool, curr_length: int):
            if node is None:
                return
            self.count = max(self.count, curr_length)
            if isLeft:
                dfs(node.right, False, curr_length + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, curr_length + 1)
                dfs(node.right, False, 1)

        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return self.count


def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


if __name__ == "__main__":
    lst = [1, None, 2, 3, 4, None, None, 5, 6, None, 7, None, None, None, 8]
    root = to_binary_tree(lst)
    print(Solution().longestZigZag(root))
