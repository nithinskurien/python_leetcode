class Solution:
    def numTilings(self, n: int) -> int:
        memo = []
        MOD = 10 ** 9 + 7
        for row in range(n + 1):
            temp = []
            for column in range(n + 1):
                temp.append(None)
            memo.append(temp)
        memo[0][0] = 1

        def dp(top: int, bottom: int) -> int:
            if top < 0 or bottom < 0:
                return 0
            if memo[top][bottom] is not None:
                return memo[top][bottom]

            count = 0
            if top == bottom:
                count += dp(top - 1, bottom - 1) + dp(top - 2, bottom - 2) + dp(top - 2, bottom - 1) + dp(top - 1,
                                                                                                          bottom - 2)
            elif top > bottom:
                count += dp(top - 2, bottom - 1) + dp(top - 2, bottom)

            else:
                count += dp(top - 1, bottom - 2) + dp(top, bottom - 2)
            memo[top][bottom] = count
            return count

        dp(n, n)
        return memo[n][n] % MOD


if __name__ == "__main__":
    print(Solution().numTilings(3))
