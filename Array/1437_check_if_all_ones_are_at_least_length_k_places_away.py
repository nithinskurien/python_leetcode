# 1437. Check If All 1's Are at Least Length K Places Away
#
# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other,
# otherwise return false.
#
#
#
# Example 1:
#
#
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:
#
#
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= k <= nums.length
# nums[i] is 0 or 1
#
# Logic:
# We just need to find the consecutive zeros between 2 ones and check if it is lesser than k if in zeros between the
# ones are less than k we return False if we iterate over nums and not have returned False we can return True. We could
# Start the nums with a one to pass that default case we can initialise the zeros to be k.

class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        zeros = k
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                if zeros < k:
                    return False
                zeros = 0
        return True