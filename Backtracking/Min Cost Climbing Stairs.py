from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # ls = [0 for i in range(len(cost)+1)]
        # for i in range(2, len(cost)+1):
        #    ls[i] = min(ls[i-1] + cost[i-1], ls[i-2] + cost[i-2])
        # return ls[-1]

        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])