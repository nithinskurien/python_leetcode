# 202. Happy Number
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process
# until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
#
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
#
# Input: n = 2
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 231 - 1
#
# Logic:
# We can iteratively add the number to a set of seen numbers and then calculate the sum of the digits of the number.
# We can keep doing this till the number is greater than one or the number we currently have is not in the seen set. If
# we see a number that is in the seen set that means we are in a loop, so we can exit. If the number after exiting the
# loop is one we return true else we return false.

class Solution:
    def isHappy(self, n: int) -> bool:
        seen_number = set()

        def digit_sum(num):
            total = 0
            while num > 0:
                total += (num % 10) ** 2
                num //= 10
            return total

        while n > 1 and n not in seen_number:
            seen_number.add(n)
            n = digit_sum(n)

        return n == 1
