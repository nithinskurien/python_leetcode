import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = zip(nums1, nums2)
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        heap = []
        currSum = 0
        maxScore = 0
        for num1, num2 in pairs:
            heapq.heappush(heap, num1)
            currSum += num1
            if len(heap) > k:
                currSum -= heapq.heappop(heap)
            if len(heap) == k:
                maxScore = max(maxScore, currSum * num2)
        return maxScore


if __name__ == "__main__":
    print(Solution().maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))
