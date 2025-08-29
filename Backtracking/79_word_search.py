# 79. Word Search
#
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.
#
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
# Follow up: Could you use search pruning to make your solution faster with a larger board?
#
# Logic:
# We need to loop through the matrix to find the first character of the word, once we find the character we will
# recursively call dfs to find the next character and so on. Everytime we visit a cell we will mark it with an ! so that
# it is marked as seen. After checking a certain path we need to backtrack and reset the board to the original state to
# continue the search



class Solution:
    def __init__(self):
        self.word = None
        self.board = None

    def dfs(self, row: int, col: int, index: int) -> bool:
        if index >= len(self.word):
            return True
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]) or self.board[row][col] != \
                self.word[index]:
            return False
        currentCharacter = self.board[row][col]
        self.board[row][col] = "!"
        found = self.dfs(row - 1, col, index + 1) or self.dfs(row + 1, col, index + 1) or self.dfs(row, col - 1,
                                                                                                   index + 1) or self.dfs(
            row, col + 1, index + 1)
        self.board[row][col] = currentCharacter
        return found

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board = board
        self.word = word
        rows, cols = len(self.board), len(self.board[0])
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == self.word[0] and self.dfs(row, col, 0):
                    return True
        return False
