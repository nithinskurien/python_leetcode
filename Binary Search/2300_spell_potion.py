class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        successList = []
        for spell in spells:
            left, right = 0, len(potions) - 1
            while left <= right:
                middle = (left + right) // 2
                if potions[middle] * spell >= success:
                    right = middle - 1
                else:
                    left = middle + 1
            successList.append(len(potions) - left)

        return successList


if __name__ == "__main__":
    print(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
