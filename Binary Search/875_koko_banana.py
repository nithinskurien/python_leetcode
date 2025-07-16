class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            middle = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += pile // middle
                if pile % middle != 0:
                    hours += 1
            if hours <= h:
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
