from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = count = 0

        while r < len(nums) - 1:
            count += 1
            mx = 1
            for i in range(l, r + 1):
                mx = max(i + nums[i], mx)
            l = r + 1
            r = mx
        return count