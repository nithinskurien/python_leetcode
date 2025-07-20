class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for index in range(len(word1) + 1):
            memo[0][index] = index
        for index in range(len(word2) + 1):
            memo[index][0] = index
        for row in range(1, len(memo)):
            for col in range(1, len(memo[0])):
                if word2[row - 1] == word1[col - 1]:
                    memo[row][col] = memo[row - 1][col - 1]
                else:
                    memo[row][col] = min(memo[row - 1][col], memo[row][col - 1], memo[row - 1][col - 1]) + 1
        return memo[-1][-1]