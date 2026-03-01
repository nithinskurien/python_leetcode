# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
#
# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For
# example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
#
# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary
# numbers needed so that they sum up to n.
#
#
#
# Example 1:
#
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32
# Example 2:
#
# Input: n = "82734"
# Output: 8
# Example 3:
#
# Input: n = "27346209830709182346"
# Output: 9
#
#
# Constraints:
#
# 1 <= n.length <= 105
# n consists of only digits.
# n does not contain any leading zeros and represents a positive integer.
#
# Logic:
# As the numbers for the deci-binary is either '1' or '0' we can recreate the digits of the actual sting using the same
# number of partitions i.e if the number is 32 we can make 30 with 3 10's and 2 with 2 1's so if we include the ones in
# the 10 we get 2 11's and one 10. similarly if the number is 23 we can get 20 with 2 10's and 3 with 3 1's including
# the 2 1's to 10 we get 2 11's and 1 1. So the solution boils down to finding the max int in the array as we just need
# that many partitions.

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
