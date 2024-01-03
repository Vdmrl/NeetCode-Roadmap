from functools import lru_cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n**2)
        # O(1)
        count = 0

        def maxPalindrome(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for mid in range(len(s)):
            # even
            if mid + 1 < len(s) and s[mid] == s[mid + 1]:
                maxPalindrome(mid, mid + 1)
            # odd
            maxPalindrome(mid, mid)
        return count
