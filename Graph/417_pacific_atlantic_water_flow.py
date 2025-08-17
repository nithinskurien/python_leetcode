# 417. Pacific Atlantic Water Flow
#
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean
# touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[
# r][c] represents the height above sea level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east,
# and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from
# any cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (
# ri, ci) to both the Pacific and Atlantic oceans.
#
#
#
# Example 1:
#
#
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:
#
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
#
#
# Constraints:
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105
#
# Logic: We can reverse the logic to instead check which cells can the oceans reach if the ocean is going uphill. So
# we can initialise two boolean matrix array for each ocean to see if the ocean can reach that cell. We can then for
# each ocean start from the border cells that touch the ocean. We can then use a recursive dfs algorithm to check if
# we can move up from the current cell to a higher cell from the current position in all the directions. We also do
# not need to check if the cell is already reachable. Once we have done the traversal check for both the oceans we just
# have to check if a particular cell is reachable form both oceans, and if they are then we return the list of the
# row, col

class Solution:

    def dfs(self, row, col, heights, ocean):
        ocean[row][col] = True
        combinations = [[row + 1, col], [row - 1, col], [row, col - 1], [row, col + 1]]
        for rowIndex, colIndex in combinations:
            if (0 <= rowIndex < len(heights) and 0 <= colIndex < len(heights[0])
                    and not ocean[rowIndex][colIndex] and heights[rowIndex][colIndex] >= heights[row][col]):
                self.dfs(rowIndex, colIndex, heights, ocean)
        return

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        result = []
        rows = len(heights)
        cols = len(heights[0])
        pacific = [[False for i in range(cols)] for j in range(rows)]
        atlantic = [[False for i in range(cols)] for j in range(rows)]

        for row in range(rows):
            self.dfs(row, 0, heights, pacific)
            self.dfs(row, cols - 1, heights, atlantic)

        for col in range(cols):
            self.dfs(0, col, heights, pacific)
            self.dfs(rows - 1, col, heights, atlantic)

        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])

        return result


if __name__ == "__main__":
    print(Solution().pacificAtlantic(
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
