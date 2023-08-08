from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 460 ms 99%
        # 29 mb 93%
        lp = 0
        rp = len(height)-1
        max_area = 0
        max_height = max(height)
        while rp > lp and (rp-lp) * max_height > max_area:
            max_area = max(min(height[lp], height[rp])*(rp-lp), max_area)
            if height[lp] > height[rp]:
                rp -= 1
            else:
                lp += 1
        return max_area