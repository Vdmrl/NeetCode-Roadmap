from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 59ms 97%
        # 16.3mb 99%
        target = Counter(s1)
        dc = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if s2[r] in target.keys():
                dc[s2[r]] += 1
                while dc[s2[r]] > target[s2[r]] or l < r:
                    dc[s2[l]] -= 1
                    l += 1
                if dc == target:
                    return True
            else:
                l = r + 1
                dc = defaultdict(int)
        return False
