from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n*n!) - 35ms - 97%
        # O(n!) - 17.36mb - 5%
        ans = []

        def dfs(cur: List[int], need: List[int]) -> None:
            if need:
                for i in range(len(need)):
                    temp = need.copy()
                    temp.pop(i)
                    dfs(cur + [need[i]], temp)
            else:
                ans.append(cur)

        dfs([], nums)
        return ans