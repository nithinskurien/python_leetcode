from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict_word1 = defaultdict(int)
        dict_word2 = defaultdict(int)
        for character in word1:
            dict_word1[character] += 1
        for character in word2:
            dict_word2[character] += 1
        if dict_word1.keys() != dict_word2.keys():
            return False
        if sorted(dict_word1.values()) != sorted(dict_word2.values()):
            return False
        return True



if __name__ == "__main__":
    solution = Solution()
    print(solution.closeStrings("a", "aa"))