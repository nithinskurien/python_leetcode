# 3186. Maximum Total Damage With Spell Casting
#
# A magician has various spells.
#
# You are given an array power, where each element represents the damage of a spell. Multiple spells can have the
# same damage value.
#
# It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell
# with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
#
# Each spell can be cast only once.
#
# Return the maximum possible total damage that a magician can cast.
#
#
#
# Example 1:
#
# Input: power = [1,1,3,4]
#
# Output: 6
#
# Explanation:
#
# The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.
#
# Example 2:
#
# Input: power = [7,1,6,6]
#
# Output: 13
#
# Explanation:
#
# The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
#
#
#
# Constraints:
#
# 1 <= power.length <= 105
# 1 <= power[i] <= 109
#
# Logic:
# We can use dp to solve the problem. We can get the counter/histogram of the spell power and it's occurrences. We can
# the get the unique power and initialise the dp array. we can initialise 2 pointers i to iterate over the unique array
# every time and j to iterate to the point which is valid for the current case. The index of the dp array will give the
# max power possible at that power index. We can then use the computed max to iterate the unique array and compute the
# max of current index.


from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        freq = Counter(power)
        unique = sorted(list(freq.keys()))
        n = len(unique)
        dp = [0] * n

        max_power = 0
        j = 0
        for i in range(n):
            while j < i and unique[j] < unique[i] - 2:
                max_power = max(max_power, dp[j])
                j += 1
            dp[i] = max_power + unique[i] * freq[unique[i]]
        return max(dp)


if __name__ == "__main__":
    print(Solution().maximumTotalDamage([1, 1, 3, 4]))
