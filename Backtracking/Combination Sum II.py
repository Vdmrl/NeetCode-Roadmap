from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(N*N^(M/min_cand + 1)) - 52ms - 87%
        # O(M*M/min_cand) - 17.2mb - 10%
        ans = []
        candidates.sort()

        def dfs(left: int, cur: List[int], need: int) -> None:
            if left < len(candidates):

                if need == candidates[left]:
                    ans.append(cur + [candidates[left]])
                elif candidates[left] <= need:
                    dfs(left+1, cur + [candidates[left]], need - candidates[left])
                while left < len(candidates) - 1 and candidates[left] == candidates[left + 1]:
                    left += 1
                dfs(left + 1, cur, need)

        dfs(0, [], target)
        return ans
