from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n)
        # 1009ms 99%
        # 39.4mb 85%
        ans = [0] * len(temperatures)
        stack = [] # indexes
        for i in temperatures:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans