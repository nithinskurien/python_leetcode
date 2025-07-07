class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = curr_vowels = 0
        for index in range(len(s)):
            if s[index] in vowels:
                curr_vowels += 1
            if index > k - 1:
                if s[index - k] in vowels:
                    curr_vowels -= 1
            max_vowels = max(curr_vowels, max_vowels)
        return max_vowels



if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels("abciiidef", 3))
