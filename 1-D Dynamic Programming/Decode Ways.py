from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        dc = set(map(str, range(1, 26 + 1)))

        @lru_cache()
        def ways(start: int) -> int:

            if start >= len(s):
                return 1
            current_count = 0
            # two element
            if start + 1 < len(s):
                if s[start:start + 2] in dc:
                    current_count += ways(start + 2)
            # one element
            if s[start] in dc:
                current_count += ways(start + 1)
            return current_count

        return ways(0)