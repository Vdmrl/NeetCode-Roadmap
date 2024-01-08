from typing import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sum(nums) % 2 == 1:
            return False
        target = sm / 2

        st = set()
        st.add(nums[0])
        for i in range(1, len(nums)):
            for j in list(st):
                st.add(j + nums[i])
            st.add(nums[i])
            if target in st:
                return True
        return False
