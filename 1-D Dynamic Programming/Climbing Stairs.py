class Solution:
    def climbStairs(self, n: int) -> int:
        # 0(n) - 39ms - 47%
        # O(1) - 16mb - 96%
        p, pp = 1,1
        if n == 1:
            return pp
        for i in range(1, n):
            t = pp
            pp = p + pp
            p = t
        return pp