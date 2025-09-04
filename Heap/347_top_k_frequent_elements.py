# 347. Top K Frequent Elements
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
# order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
#
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
#
# Output: [1]
#
# Example 3:
#
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#
# Output: [1,2]
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#
# Logic:
# We first will get frequency of the numbers with the help of a hashmap, we will then use a heap of size k to keep the
# k largest occurrences. We will add to the heap if the size is less than k or the occurrence at the start of the heap
# is lesser than what we want to append. We will then later check if the heap is larger than k and if so we will pop
# removing the smaller occurrence. We will in the end return the k values.

import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        heap = []
        for key, val in hashmap.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]
