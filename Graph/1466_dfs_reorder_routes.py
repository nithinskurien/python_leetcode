from collections import defaultdict

class Solution:
    def __init__(self):
        self.visitedNodes = None

    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        stack = [0]
        self.visitedNodes = set()
        nodeSet = set()
        nodeDict = defaultdict(list)
        for start, end in connections:
            nodeDict[start].append(end)
            nodeDict[end].append(start)
            nodeSet.add((start, end))
        reverseDirectionCount = 0
        while stack:
            currNode = stack.pop()
            if currNode not in self.visitedNodes:
                for node in nodeDict[currNode]:
                    if (currNode, node) in nodeSet and node not in self.visitedNodes:
                        reverseDirectionCount += 1
                    stack.append(node)
            self.visitedNodes.add(currNode)
        return reverseDirectionCount


if __name__=="__main__":
    print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))