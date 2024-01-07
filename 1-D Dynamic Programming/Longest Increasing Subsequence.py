from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP - O(n**2)
        # DP - O(n)
        prev = [1 for i in range(nums)]
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    prev[i] = max(prev[i],prev[j]+1)
        return prev[0]

