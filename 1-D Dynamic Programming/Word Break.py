from typing import List
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dfs memoization
        # O(n * m + k)
        # O(n + k)
        words = set(wordDict)
        @lru_cache()
        def is_segmented(start: int) -> bool:
            if start >= len(s):
                return True
            accum = ""
            for i in range(start, len(s)):
                accum += s[i]
                if accum in words and is_segmented(i + 1):
                    return True
        return is_segmented(0)







