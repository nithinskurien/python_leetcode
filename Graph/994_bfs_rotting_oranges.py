from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        rottingOranges = [(row, col) for row, matrix in enumerate(grid) for col, val in enumerate(matrix) if val == 2]
        queue = deque()
        queue.extend(rottingOranges)
        count = 0
        if not any(1 in row for row in grid):
            return 0
        while queue:
            currLength = len(queue)
            for index in range(currLength):
                row, col = queue.popleft()
                directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for dirRow, dirCol in directions:
                    point = (dirRow, dirCol)
                    if 0 <= dirRow < rowCount and 0 <= dirCol < colCount and grid[dirRow][dirCol] == 1:
                        queue.append(point)
                        grid[dirRow][dirCol] = 2
            count += 1
            if not any(1 in row for row in grid):
                return count
        return -1

if __name__ == "__main__":
    print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))