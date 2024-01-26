from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = cur = nums[0]
        for i in nums[1:]:
            cur = max(cur + i, i)
            mx = max(mx, cur)
        return mx