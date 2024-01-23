from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = []
        for i in range(n+1):
            if i == 0:
                ls.append(0)
            elif i == 1:
                ls.append(1)