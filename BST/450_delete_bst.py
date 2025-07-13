from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.parentNode = None
        self.nodeQueue = None

    def rebuildSubTree(self, node: TreeNode) -> TreeNode:
        if not node or (not node.left and not node.right):
            return None
        if not node.left:
            return node.right
        currNode = node.left
        if not currNode:
            return currNode.right
        while currNode.right:
            currNode = currNode.right
        currNode.right = node.right
        return node.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.rootNode = root
        def search(node: TreeNode, parent: TreeNode):
            if not node:
                return
            if node.val > key:
                search(node.left, node)
            elif node.val < key:
                search(node.right, node)
            else:
                if not parent:
                    if not node.left and not node.right:
                        self.rootNode = None
                        return
                    else:
                        self.rootNode = self.rebuildSubTree(node)
                        return
                if key < parent.val:
                    parent.left = self.rebuildSubTree(node)
                else:
                    parent.right = self.rebuildSubTree(node)
        search(root, None)
        return self.rootNode


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
    #lst = [5, 3, 6, 2, 4, None, 7]
    #lst = [5,3,6,2,4,None,7]
    #lst = [0]
    lst = [1,None,2]
    test = to_binary_tree(lst)
    print(Solution().deleteNode(test, 1))
