class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        current_string = ""
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                current_string = ""
                num = ""
                while stack and stack[-1] != '[':
                    current_string = stack.pop() + current_string
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(current_string * int(num))

        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a2[c]]"))
