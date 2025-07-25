# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for
# the current day.
#
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and
# going backward) for which the stock price was less than or equal to the price of that day.
#
# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2,
# then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4
# consecutive days. Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock
# today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal
# 8 for 3 consecutive days. Implement the StockSpanner class:
#
# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
#
#
# Example 1:
#
# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]
#
# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6

# The solution uses a stack to keep track of previous prices and how many days each one covered.
# 
# When a new price comes in:
# Start with a count of 1 (for today).
# If the new price is greater than or equal to prices on top of the stack, those earlier prices are no longer useful
# for future comparisons.
# So, pop them off and add their counts to today's count (because today is part of a longer streak of higher or equal
# prices). After combining those, push the current price along with its total count onto the stack. Finally,
# return the count — that’s the number of consecutive days (including today) the price has not dropped.

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            prevPrice, prevCount = self.stack.pop()
            count += prevCount
        self.stack.append((price, count))
        return count