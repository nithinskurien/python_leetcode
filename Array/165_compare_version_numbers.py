# 165. Compare Version Numbers
#
# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by
# dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
#
# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has
# fewer revisions, treat the missing revision values as 0.
#
# Return the following:
#
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
#
#
# Example 1:
#
# Input: version1 = "1.2", version2 = "1.10"
#
# Output: -1
#
# Explanation:
#
# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.
#
# Example 2:
#
# Input: version1 = "1.01", version2 = "1.001"
#
# Output: 0
#
# Explanation:
#
# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
#
# Example 3:
#
# Input: version1 = "1.0", version2 = "1.0.0.0"
#
# Output: 0
#
# Explanation:
#
# version1 has less revisions, which means every missing revision are treated as "0".
#
#
#
# Constraints:
#
# 1 <= version1.length, version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a 32-bit integer.
#
# Logic:
# We can split the version numbers at '.' to give a list. We can then pad the vesion number with less dots with zero to
# match the one with more dots for e.g 1.0 vs 1.1.0.0 we can pad 1.0 to 1.0.0.0 and then we can compare the list values
# to return 1, -1 or 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1List = version1.split('.')
        ver2List = version2.split('.')
        for index in range(max(len(ver1List), len(ver2List))):
            v1 = int(ver1List[index]) if index < len(ver1List) else 0
            v2 = int(ver2List[index]) if index < len(ver2List) else 0
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
        return 0
