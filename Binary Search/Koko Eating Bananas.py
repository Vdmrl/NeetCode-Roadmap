from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 302ms 96%
        # 17.8mb 77%
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            m = (l + r) // 2
            current_h = 0
            for i in piles:
                current_h += ceil(i / m)
            if current_h <= h:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        return ans
