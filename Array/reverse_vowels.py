class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left_pointer = 0
        right_pointer = len(s) - 1
        answer = list(s)
        if len(s) <= 1:
            return s
        while left_pointer < right_pointer:
            if answer[left_pointer] not in vowels:
                left_pointer = min(len(s) - 1, left_pointer + 1)
            elif answer[right_pointer] not in vowels:
                right_pointer = max(0, right_pointer - 1)
            else:
                temp = answer[right_pointer]
                answer[right_pointer] = answer[left_pointer]
                answer[left_pointer] = temp
                left_pointer = min(len(s) - 1, left_pointer + 1)
                right_pointer = max(0, right_pointer - 1)

        return "".join(answer)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse_vowels("race a car"))
