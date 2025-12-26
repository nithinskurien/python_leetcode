# 2483. Minimum Penalty for a Shop
#
# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of
# characters 'N' and 'Y':
#
# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
#
# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
#
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
#
#
#
# Example 1:
#
# Input: customers = "YYNY"
# Output: 2
# Explanation:
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
# Example 2:
#
# Input: customers = "NNNNN"
# Output: 0
# Explanation: It is best to close the shop at the 0th hour as no customers arrive.
# Example 3:
#
# Input: customers = "YYYY"
# Output: 4
# Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
#
#
# Constraints:
#
# 1 <= customers.length <= 105
# customers consists only of characters 'Y' and 'N'.
#
# Logic:
# We do not need to know the absolute penalty, so we can get away with finding the relative penalty. We can iterate over
# the customers array and decrease the penalty if the customer is 'Y' assuming that we were open so we did not incurr a
# penalty or increase the penalty if the cutomer is 'N' and every time we can check if the currPenalty is lesser than
# minPenalty. If yes we store the index + 1 as result and replace the minPenalty.

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        res = 0
        minPenalty = 0
        currPenalty = 0
        for index, customer in enumerate(customers):
            if customer == 'Y':
                currPenalty -= 1
            else:
                currPenalty += 1

            if currPenalty < minPenalty:
                minPenalty = currPenalty
                res = index + 1
        return res