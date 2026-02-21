# Q2. Evaluate Reverse Polish Notation
#
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
#
#
# Example 1:
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
# Logic:
# We can create a stack and append elements till a symbol is reached if that happens we can pop 2 values from the stack
# do the operation and append it back. Once we have iterated over all the tokens we can return the last element.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        sym = {'+', '-', '*', '/'}
        ans = []
        for token in tokens:
            if token in sym:
                op_b = int(ans.pop())
                op_a = int(ans.pop())
                if token == '+':
                    ans.append(op_a + op_b)
                elif token == '-':
                    ans.append(op_a - op_b)
                elif token == '*':
                    ans.append(op_a * op_b)
                else:
                    ans.append(op_a / op_b)
            else:
                ans.append(token)
        return ans[0]

if __name__=="__main__":
    print(Solution().evalRPN(["4","13","5","/","+"]))