# 401. Binary Watch
#
# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the
# minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the below binary watch reads "4:51".
#
#
# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all
# possible times the watch could represent. You may return the answer in any order.
#
# The hour must not contain a leading zero.
#
# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.
#
# For example, "10:2" is not valid. It should be "10:02".
#
#
# Example 1:
#
# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:
#
# Input: turnedOn = 9
# Output: []
#
#
# Constraints:
#
# 0 <= turnedOn <= 10
#
# Logic:
# We can have nested loops to iterate over all the possible hour, min combination and then check the number of bits
# needed to represent that time and if that is equal to the turnedOn number we can add it to the result.

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        for hours in range(12):
            for mins in range(60):
                if hours.bit_count() + mins.bit_count() == turnedOn:
                    h = str(hours)
                    m = '0' + str(mins) if mins < 10 else str(mins)
                    res.append(h + ':' + m)
        return res