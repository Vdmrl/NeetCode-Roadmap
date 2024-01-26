from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums), -1, -1):
            if nums[i] + i >= target:
                target = i
        return target == 0
