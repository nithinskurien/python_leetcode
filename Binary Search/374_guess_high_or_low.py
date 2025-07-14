class Solution:
    def guessNumber(self, n:int) -> int:
        low, high = 1, n
        while low < high:
            middle = (low + high)//2
            guessed = guess(middle)
            if guessed == -1:
                high = middle - 1
            elif guessed == 1:
                low = middle + 1
            else:
                return middle

        return low