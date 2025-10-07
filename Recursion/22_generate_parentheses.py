# 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8
#
# Logic:
# We know that we can only use close brackets when the number of open brackets is lesser than close. We can recursively
# create the solution such that the base case is when the number of open & close brackets is zero. When we reach the
# base case we can append the generated string of parentheses to the result. Else we can recursively add the open or
# close bracket

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def generate(open: int, close: int, curr: str):
            if open == 0 and close == 0:
                result.append(curr)
                return
            if open > 0:
                generate(open - 1, close, curr + '(')
            if open < close:
                generate(open, close - 1, curr + ')')

        generate(n, n, "")

        return result
