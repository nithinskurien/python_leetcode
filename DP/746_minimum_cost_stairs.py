class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        totalSteps = len(cost)

        def dpMinNextStepCost(currStep: int):
            if currStep > len(cost) - 1:
                return
            cost[currStep] += min(cost[currStep - 1], cost[currStep - 2])
            dpMinNextStepCost(currStep + 1)

        dpMinNextStepCost(2)
        return min(cost[totalSteps - 1], cost[totalSteps - 2])

if __name__=="__main__":
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

