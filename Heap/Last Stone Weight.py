from typing import List
import heapq



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if y != x:
                heapq.heappush(stones, y - x)
        if stones:
            return -stones[0]
        else:
            return 0
