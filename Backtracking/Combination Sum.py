from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(N^(M/min_cand + 1)) - 43ms - 98%
        # O(M/min_cand) - 17.43mb - 5%
        ans = []

        def dfs(left: int, cur: List[int], need: int) -> None:
            if left < len(candidates):
                dfs(left + 1, cur, need)
                if need == candidates[left]:
                    ans.append(cur + [candidates[left]])
                elif candidates[left] <= need:
                    dfs(left, cur + [candidates[left]], need - candidates[left])

        dfs(0, [], target)
        return ans
