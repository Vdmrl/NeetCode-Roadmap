from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(nums):
            reside = target - val
            if val in dic:
                return [dic[val], i]
            dic[reside] = i
