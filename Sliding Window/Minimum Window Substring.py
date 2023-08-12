from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 147ms 54%
        # 17.1mb 95%
        min_st, c, target_length, length, l = [-1, -1], Counter(t), len(t), 0, 0
        for r in range(len(s)):
            if s[r] in c.keys():
                c[s[r]] -= 1
                if c[s[r]] >= 0:
                    length += 1
            while l < r and (s[l] not in c.keys() or c[s[l]] < 0):
                if s[l] in c.keys():
                    c[s[l]] += 1
                    if c[s[l]] > 0:
                        length -= 1
                l += 1
            if length == target_length:
                if min_st[0] == -1 or r - l + 1 < min_st[1] - min_st[0] + 1:
                    min_st = [l, r]
        if min_st[0] == -1:
            return ""
        else:
            return s[min_st[0]:min_st[1] + 1]
