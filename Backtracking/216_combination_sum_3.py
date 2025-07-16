class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        output = []

        def recursive(start: int, subset: list):
            currSum = 0
            if subset:
                currSum = sum(subset)
                if currSum > n:
                    return
                if len(subset) >= k:
                    if currSum == n:
                        output.append(list(subset))
                    return
            for num in range(start, 10):
                subset.append(num)
                recursive(num + 1, subset)
                subset.pop()

        recursive(1, [])
        return output


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))
