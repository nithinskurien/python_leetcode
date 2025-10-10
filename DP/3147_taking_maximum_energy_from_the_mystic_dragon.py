# 3147. Taking Maximum Energy From the Mystic Dungeon
#
# In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some
# magicians can give you negative energy, which means taking energy from you.
#
# You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported
# to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.
#
# In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the
# magicians' sequence, absorbing all the energy during the journey.
#
# You are given an array energy and an integer k. Return the maximum possible energy you can gain.
#
# Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.
#
#
#
# Example 1:
#
# Input: energy = [5,2,-10,-5,1], k = 3
#
# Output: 3
#
# Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.
#
# Example 2:
#
# Input: energy = [-2,-3,-1], k = 2
#
# Output: -1
#
# Explanation: We can gain a total energy of -1 by starting from magician 2.
#
#
#
# Constraints:
#
# 1 <= energy.length <= 105
# -1000 <= energy[i] <= 1000
# 1 <= k <= energy.length - 1
#
# Logic:
# We can start from the kth last element of the energy array and then compute the energy if we were to start at that
# position by energy[i] = energy[i] + energy[i + k], we can then iteratively go backwards till the first position. We
# now have an array of modified energy where the values represent the total energy we would get if we start at that
# position. We can then take the max of the array and return that value.

class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
