from typing import List
from functools import lru_cache

class Solution:

    @staticmethod
    @lru_cache()
    def is_palindrome(s: str, l: int, r: int) -> bool:
        while s[l] == s[r]:
            if l >= r:
                return True
            l += 1
            r -= 1
        return False

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []

        def dfs(size: int) -> None:
            if size >= len(s):
                ans.append(cur.copy())
                return
            for start in range(size, len(s)):
                if not Solution.is_palindrome(s, size, start):
                    continue
                cur.append(s[size:start + 1])
                dfs(start + 1)
                cur.pop()

        dfs(0)
        return ans