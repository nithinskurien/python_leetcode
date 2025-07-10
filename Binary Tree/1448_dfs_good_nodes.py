class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.count = None

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def goodNodesRec(root: TreeNode, max_root: int):
            if root.val >= max_root:
                self.count += 1
            if root.left:
                goodNodesRec(root.left, max(max_root, root.left.val))
            if root.right:
                goodNodesRec(root.right, max(max_root, root.right.val))

        goodNodesRec(root, root.val)
        return self.count
