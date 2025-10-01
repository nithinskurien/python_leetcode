# 1518. Water Bottles
#
# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water
# bottles from the market with one full water bottle.
#
# The operation of drinking a full water bottle turns it into an empty bottle.
#
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
#
#
#
# Example 1:
#
#
# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.
# Example 2:
#
#
# Input: numBottles = 15, numExchange = 4
# Output: 19
# Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 15 + 3 + 1 = 19.
#
#
# Constraints:
#
# 1 <= numBottles <= 100
# 2 <= numExchange <= 100
#
# Logic:
# We will keep exchanging empty bottles till we cannot exchange any bottles anymore. We will add the bottles that are
# full to the result and keep track of the bottles that cannot be exchanged as a remainder that gets carried over to the
# next stage of the iteration.

class Solution:
        def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
            res = numBottles
            while numBottles >= numExchange:
                remainder = numBottles % numExchange
                numBottles = numBottles // numExchange
                res += numBottles
                numBottles += remainder
            return res


if __name__=="__main__":
    print(Solution().numWaterBottles(15, 4))