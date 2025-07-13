class Solution:
    def __init__(self):
        self.provinces = None
        self.visitedNodes = None
        self.stack = None

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        self.stack = []
        self.visitedNodes = set()
        self.provinces = 0
        for index in range(len(isConnected)):
            if index not in self.visitedNodes:
                self.stack.append(index)
                self.provinces += 1
            while self.stack:
                currNode = self.stack.pop()
                if currNode not in self.visitedNodes:
                    self.visitedNodes.add(currNode)
                    for index in range(len(isConnected[currNode])):
                        if index not in self.visitedNodes and isConnected[currNode][index] == 1:
                            self.stack.append(index)
        return self.provinces


if __name__ == "__main__":
    print(Solution().findCircleNum([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]))
