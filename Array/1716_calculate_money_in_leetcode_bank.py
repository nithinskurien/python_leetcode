# 1716. Calculate Money in Leetcode Bank
#
# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than
# the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
#
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
#
#
#
# Example 1:
#
# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
# Example 2:
#
# Input: n = 10 Output: 37 Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) =
# 37. Notice that on the 2nd Monday, Hercy only puts in $2. Example 3:
#
# Input: n = 20 Output: 96 Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5
# + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
#
#
# Constraints:
#
# 1 <= n <= 1000
#
# Logic:
# We can create an array initialised with element 1 to represent the amount for the first day and sum as 1. We can
# iterate from 1 to n and check if the day is a Monday by checking of the remainder with 7 is 0. If it is we can add one
# to the seventh last element in amount, if the day is not Monday we can just add 1 to the last element in amount. At
# each iteration we can append last element of amount to sum and return


class Solution:
    def totalMoney(self, n: int) -> int:
        amount = [1]
        sum = 1
        for day in range(1, n):
            if day % 7 == 0:
                amount.append(amount[-7] + 1)
            else:
                amount.append(amount[-1] + 1)
            sum += amount[-1]
        return sum


if __name__ == "__main__":
    print(Solution().totalMoney(20))
