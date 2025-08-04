# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
#
# Logic: We will iterate over the characters in a string and keep appending to the stack when we see an open bracket,
# as soon as we see a close bracket we will pop from the stack and see if the popped character is the mirrored open
# bracket if is not we will return false. In the end we will return if the len of stack is zero. If were not able to
# close all the open brackets there would still be elements left in the stack which should return false.

class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if stack and char in map:
                poppedChar = stack.pop()
                if not poppedChar == map[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
