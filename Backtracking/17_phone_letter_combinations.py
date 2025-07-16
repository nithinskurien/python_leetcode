class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {'2': ('a', 'b', 'c'),
                   '3': ('d', 'e', 'f'),
                   '4': ('g', 'h', 'i'),
                   '5': ('j', 'k', 'l'),
                   '6': ('m', 'n', 'o'),
                   '7': ('p', 'q', 'r', 's'),
                   '8': ('t', 'u', 'v'),
                   '9': ('w', 'x', 'y', 'z')}
        combinations = [""]
        if digits == "":
            return []
        for digit in digits:
            temp = []
            for char in mapping[digit]:
                for comb in combinations:
                    temp.append(comb + char)
            combinations = temp
        return combinations

    def letterCombinationsRecursive(self, digits: str) -> list[str]:
        mapping = {'2': ('a', 'b', 'c'),
                   '3': ('d', 'e', 'f'),
                   '4': ('g', 'h', 'i'),
                   '5': ('j', 'k', 'l'),
                   '6': ('m', 'n', 'o'),
                   '7': ('p', 'q', 'r', 's'),
                   '8': ('t', 'u', 'v'),
                   '9': ('w', 'x', 'y', 'z')}
        combinations = []

        if digits == "":
            return []

        def recursive(curr: str, digitIndex: int):
            if digitIndex >= len(digits):
                combinations.append(curr)
                return
            else:
                for char in mapping[digits[digitIndex]]:
                    recursive(curr + char, digitIndex + 1)
        recursive("", 0)
        return combinations

if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinationsRecursive("23"))
