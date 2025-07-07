from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_dict = defaultdict(int)
        pairs = 0
        length = len(grid)
        for row_index in grid:
            row_dict[tuple(row_index)] += 1
        for column_index in range(length):
            column_substring = tuple(grid[row_index][column_index] for row_index in range(length))
            if column_substring in row_dict:
                pairs += row_dict[column_substring]
        return pairs

if __name__ == "__main__":
    solution = Solution()
    print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))