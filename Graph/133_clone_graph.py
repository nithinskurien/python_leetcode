# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
#
# Test case format:
#
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val
# == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
#
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set
# of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a
# reference to the cloned graph.
#
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:
#
#
# Input: adjList = [[]] Output: [[]] Explanation: Note that the input contains one empty list. The graph consists of
# only one node with val = 1 and it does not have any neighbors. Example 3:
#
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
#
#
# Constraints:
#
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.
#
# Logic: We can create a dict of the visited nodes as keys and the cloned nodes as value. Every time we come across a
# non visited node we can clone and add it to the dict. We can then add the children to the cloned node using the
# recursive call to clone function. The return clause for the recursive function is when the clone node is returned from
# the visited dict, and we have the neighbours also cloned. the recursive call would be to get the cloned copy of the
# neighbours as they may have not been created yet when a node is created


from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def clone(self, node):
        if node in self.visited:
            return self.visited[node]
        clonedNode = Node(node.val, None)
        self.visited[node] = clonedNode
        for neighbour in node.neighbors:
            clonedNode.neighbors.append(self.clone(neighbour))
        return clonedNode

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        return self.clone(node)


if __name__ == "__main__":
    node4 = Node(4, [])
    node3 = Node(3, [])
    node2 = Node(2, [])
    node1 = Node(1, [])
    node1.neighbors.extend([node2, node4])
    node2.neighbors.extend([node1, node3])
    node3.neighbors.extend([node2, node4])
    node4.neighbors.extend([node1, node3])
    print(Solution().cloneGraph(node1))
