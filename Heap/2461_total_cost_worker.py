import heapq


class Solution:

    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        heap = []
        totalCost = 0
        for frontPointer in range(candidates):
            heapq.heappush(heap, (costs[frontPointer], frontPointer))
        backPointer = max(frontPointer + 1, len(costs) - candidates)
        for backIndex in range(backPointer, len(costs)):
            heapq.heappush(heap, (costs[backIndex], backIndex))

        while k > 0:
            cost, index = heapq.heappop(heap)
            totalCost += cost
            k -= 1
            if frontPointer < backPointer - 1:
                if index < frontPointer:
                    frontPointer += 1
                    heapq.heappush(heap, (costs[frontPointer], frontPointer))
                else:
                    backPointer -= 1
                    heapq.heappush(heap, (costs[backPointer], backPointer))

        return totalCost
