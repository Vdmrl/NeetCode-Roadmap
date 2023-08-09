from typing import List


class Solution:
    def trap3NMem(self, height: List[int]) -> int:
        # 123 ms 80%
        # 18 mb 90%
        max_left, max_right = [0], [0]
        for i, h in enumerate(height):
            max_left.append(max(max_left[-1], h))
        for i, h in enumerate(reversed(height)):
            max_right.append(max(max_right[-1], h))
        ans = 0
        for i, h in enumerate(height):
            w = min(max_left[i], max_right[-1 - i]) - h
            if w > 0:
                ans += w
        return ans
    def trapTwoPointers(self, height: List[int]) -> int:
        # 100 ms 99%
        # 18 mb 90%
        lp, rp = 1,len(height) - 2
        max_left, max_right = height[0], height[len(height) - 1]
        ans = 0
        while lp <= rp:
            if max_left <= max_right:
                max_left = max(max_left, height[lp])
                ans += max_left - height[lp]
                lp += 1
            else:
                max_right = max(max_right, height[rp])
                ans += max_right - height[rp]
                rp -= 1
        return ans
