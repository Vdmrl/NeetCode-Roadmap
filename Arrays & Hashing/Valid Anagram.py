from collections import defaultdict
from collections import Counter


class Solution:
    def isAnagramSet(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        for i in set(s):
            if (s.count(i) != t.count(i)):
                return False
        return True

    def isAnagramDict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s:
            d1[i] += 1
        for i in t:
            d2[i] += 1
        if d1 == d2:
            return True
        return False

    def isAnagramCounter(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False
