from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # O(n*2**n) - 96% - 34ms
        # O(n*2**n) - 6% - 17.4mb

        ans = []
        nums.sort()

        def dfs(left: int, cur: List[int]) -> None:
            if left == len(nums):
                ans.append(cur)
            else:
                dfs(left + 1, cur + [nums[left]])
                while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                    left += 1
                dfs(left + 1, cur)

        dfs(0, [])
        return ans
