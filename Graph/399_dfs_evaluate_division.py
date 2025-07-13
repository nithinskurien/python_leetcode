from collections import defaultdict


class Solution:
    def __init__(self):
        self.visited = None

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        nodes = defaultdict(dict)
        self.visited = set()
        answers = []
        for index, value in enumerate(values):
            start, end = equations[index]
            nodes[start][end] = value
            nodes[end][start] = 1/value

        def dfs(source: str, dest: str, current: float) -> float:
            if source not in nodes or dest not in nodes:
                return -1
            if source == dest:
                return 1
            if dest in nodes[source]:
                return current*nodes[source][dest]
            self.visited.add(source)
            for connection in nodes[source]:
                if connection not in self.visited:
                    result = dfs(connection, dest, current * nodes[source][connection])
                    if result != -1:
                        return result
            return -1

        for start, destination in queries:
            self.visited.clear()
            answers.append(dfs(start, destination, 1))

        return answers

if __name__=="__main__":
    print(Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))

