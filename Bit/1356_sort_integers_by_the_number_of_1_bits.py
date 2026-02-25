# 1356. Sort Integers by The Number of 1 Bits
#
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their
# binary representation and in case of two or more integers have the same number of 1's you have to sort them in
# ascending order.
#
# Return the array after sorting it.
#
#
#
# Example 1:
#
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explanation: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]
# Example 2:
#
# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explanation: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
#
#
# Constraints:
#
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 104
#
# Logic:
# We can use bit_count to get the count of each number and then append the number to a list which has the key as the bit
# count. We can then iterate the key of the bit count and then sort the list and then extend the result array.

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        res = []
        map_array = {}
        for num in arr:
            bit_count = num.bit_count()
            if bit_count in map_array.keys():
                map_array[bit_count].append(num)
            else:
                map_array[bit_count] = [num]
        for key in sorted(map_array.keys()):
            res.extend(sorted(map_array[key]))
        return res