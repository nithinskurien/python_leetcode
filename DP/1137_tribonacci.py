from collections import defaultdict


class Solution:
    def __init__(self):
        self.memo = defaultdict(None)
        self.memo[0] = 0
        self.memo[1] = 1
        self.memo[2] = 1

    def tribonacci(self, n: int) -> int:
        fib = self.memo.get(n)
        if fib is not None:
            return fib
        fib = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        self.memo[n] = fib
        return self.memo[n]


class SolutionInner:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def dp(num: int) -> int:
            fib = memo.get(num)
            if fib is not None:
                return fib
            fib = dp(num - 3) + dp(num - 2) + dp(num - 1)
            memo[num] = fib
            return memo[num]

        return dp(n)


if __name__ == "__main__":
    print(Solution().tribonacci(5))
    print(SolutionInner().tribonacci(5))
