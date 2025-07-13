import sys
from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rowCount = len(maze)
        columnCount = len(maze[0])
        nodes = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while nodes:
            row, column, step = nodes.popleft()
            directions = [(row - 1, column), (row + 1, column), (row, column -1), (row, column + 1)]
            for dirRow, dirColumn in directions:
                print(dirRow, dirColumn)
                if 0 <= dirRow <= rowCount - 1 and 0 <= dirColumn <= columnCount - 1 and maze[dirRow][dirColumn] == '.':
                    if dirRow == 0 or dirRow == rowCount - 1 or dirColumn == 0 or dirColumn == columnCount - 1:
                        return step + 1
                    nodes.append((dirRow, dirColumn, step + 1))
                    maze[dirRow][dirColumn] = '+'

        return -1


if __name__ == "__main__":
    print(Solution().nearestExit([[".","+"]], [0, 0]))

