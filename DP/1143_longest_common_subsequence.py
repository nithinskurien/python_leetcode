class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(1, rows):
            for col in range(1, cols):
                if text1[row - 1] == text2[col - 1]:
                    memo[row][col] = memo[row-1][col-1] + 1
                else:
                    memo[row][col] = max(memo[row - 1][col], memo[row][col-1])
        return memo[rows - 1][cols - 1]

if __name__=="__main__":
    print(Solution().longestCommonSubsequence("abcde", "ace"))