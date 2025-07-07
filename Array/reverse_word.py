from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        word_start_pointer = 0
        word_end_pointer = 0
        answer = deque()
        while word_start_pointer < len(s):
            word = ""
            if s[word_end_pointer] == " ":
                word = s[word_start_pointer:word_end_pointer]
                if word != '' and word != ' ':
                    answer.appendleft(word)
                word_start_pointer = word_end_pointer + 1
            elif word_end_pointer == len(s) - 1:
                word = s[word_start_pointer:word_end_pointer + 1]
                if word != '' and word != ' ':
                    answer.appendleft(word)
                word_start_pointer = word_end_pointer + 1
            word_end_pointer += 1
        return " ".join(answer)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("t "))
