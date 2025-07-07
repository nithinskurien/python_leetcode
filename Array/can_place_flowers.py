class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        open_space = 0
        for index in range(len(flowerbed)):
            if flowerbed[index] == 0:
                is_left_empty = (index == 0) or (flowerbed[index-1] == 0)
                is_right_empty = (index == len(flowerbed) - 1) or (flowerbed[index+1] == 0)
                if is_left_empty and is_right_empty:
                    flowerbed[index] = 1
                    open_space += 1
                    if n <= open_space:
                        return True
        return n <= open_space


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([0, 0, 0, 0, 1], 2))
