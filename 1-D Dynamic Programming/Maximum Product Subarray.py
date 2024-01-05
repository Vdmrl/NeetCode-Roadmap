import operator
from typing import List
from functools import reduce

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(N)
        # O(1)
        global_max = nums[0]
        local_min, local_max = 1, 1
        for i in nums:
            local_max, local_min = max(local_min * i, local_max * i, i), min(local_min * i, local_max * i, i)
            global_max = max(global_max, local_max)
        return global_max

