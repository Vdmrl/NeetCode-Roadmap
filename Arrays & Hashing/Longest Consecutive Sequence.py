from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        max_len = 0
        for i in nums:
            if i + 1 not in st: # search for last
                ln = 1
                while (i - ln) in st:
                    ln += 1
                max_len = max(max_len, ln)
        return max_len