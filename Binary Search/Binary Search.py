from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            t = l + (r - l) // 2
            if nums[t] > target:
                r = t - 1
            elif nums[t] < target:
                l = t + 1
            else:
                return t
        return -1
