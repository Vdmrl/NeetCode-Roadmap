from typing import List

class Solution:
    # O(n*n**2) - 31ms - 97%
    # O(n) - 17.48mb - 8%
    def subsets(self, nums: List[int]) -> List[List[int]]:
        full = [[]]
        prev = [[]]
        for _ in nums:
            new = []
            for i in nums:
                for j in prev:
                    if not j or j[-1] < i:
                        new.append(j + [i])
            full.extend(new)
            prev = new
        return full


