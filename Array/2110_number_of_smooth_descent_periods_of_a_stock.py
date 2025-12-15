# 2110. Number of Smooth Descent Periods of a Stock
#
# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock
# price on the ith day.
#
# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower
# than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.
#
# Return the number of smooth descent periods.
#
#
#
# Example 1:
#
# Input: prices = [3,2,1,4]
# Output: 7
# Explanation: There are 7 smooth descent periods:
# [3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
# Note that a period with one day is a smooth descent period by the definition.
# Example 2:
#
# Input: prices = [8,6,7,7]
# Output: 4
# Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
# Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
# Example 3:
#
# Input: prices = [1]
# Output: 1
# Explanation: There is 1 smooth descent period: [1]
#
#
# Constraints:
#
# 1 <= prices.length <= 105
# 1 <= prices[i] <= 105
#
#
# Logic:
# We can traverse the array while keeping track of a cont_len variable. For a series e.g 3, 2, 1 the total
# possible periods ending with 1 will be the length of that sequence i.e [1], [2, 1], [3, 2, 1] similarly the periods
# ending with 2 will be [3, 2] and [2] so at every index the number of periods ending with the value in that index
# will be the length of that subsequence. So for every index we can increase the cont_len if the subsequence is still
# gradually descending of reset it to 1 if not and then add the cont_len to result.



class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        cont_len = 1
        result = 1
        for index in range(1, len(prices)):
            if prices[index - 1] - prices[index] == 1:
                cont_len += 1
            else:
                cont_len = 1
            result += cont_len
        return result
