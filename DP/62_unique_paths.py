class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None for _ in range(n)] for _ in range(m)]

        def dp(row: int, col: int) -> int:
            if memo[row][col] is not None:
                return memo[row][col]
            if row < 0 or col < 0:
                return 0
            if row == 0 or col == 0:
                return 1
            count = dp(row - 1, col) + dp(row, col - 1)
            memo[row][col] = count
            return count

        return dp(m - 1, n - 1)

if __name__=="__main__":
    print(Solution().uniquePaths(1,1))