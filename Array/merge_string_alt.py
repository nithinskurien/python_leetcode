class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        solution = ""
        for i in range(max_length):
            if i < len(word1):
                solution += word1[i]
            if i < len(word2):
                solution += word2[i]

        return solution