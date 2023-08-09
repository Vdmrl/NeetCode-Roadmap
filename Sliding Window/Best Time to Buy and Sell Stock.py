from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 828 95%
        # 27mb 98%
        mn = prices[0]
        ans = 0
        for p in prices:
            if p < mn:
                mn = p
            else:
                ans = max(ans, p-mn)
        return ans