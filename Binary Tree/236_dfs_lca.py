class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.commonAncestor = root

        def dfs(node: TreeNode) -> bool:
            if node is None:
                return False
            isNode = (node == p or node == q)
            left = dfs(node.left)
            right = dfs(node.right)
            if (left and right) or (isNode and (left or right)):
                self.commonAncestor = node
            return isNode or left or right
        dfs(root)
        return self.commonAncestor


def to_binary_tree(items, pnode, qnode):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    pnodes = None
    qnodes = None
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            if val == pnode:
                pnodes = node.left
            if val == qnode:
                qnodes = node.left
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            if val == pnode:
                pnodes = node.right
            if val == qnode:
                qnodes = node.right
            q.append(node.right)
    return root, pnodes, qnodes



if __name__ == "__main__":
    lst = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root, p, q = to_binary_tree(lst, 5, 4)
    print(Solution().lowestCommonAncestor(root, p, q).val)
