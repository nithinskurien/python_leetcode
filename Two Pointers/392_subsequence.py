class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0
        if len(s) == 0:
            return True
        while t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            if s_pointer >= len(s):
                return True
            t_pointer += 1
        return False


if __name__ == "__main__":
    solution = Solution()
