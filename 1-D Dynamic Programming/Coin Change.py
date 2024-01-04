from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # memoization solution
        # cashe = {}
        # def dfs(need: int) -> int:
        #    if need == 0:
        #        return 0
        #    elif need < 0:
        #        return float("inf")
        #    elif need in cashe:
        #        return cashe[need]
        #    cashe[need] = min(dfs(need - c) + 1 for c in coins)
        #    return cashe[need]
        # a = dfs(amount)
        # return -1 if a == float("inf") else a

        # dynamic solution
        if amount == 0:
            return 0

        ls = [-1 for i in range(amount)]

        for target in range(len(ls)):
            mn = float("inf")
            for coin in coins:
                if target + 1 == coin:
                    mn = 1
                    break
                if target - coin >= 0 and ls[target - coin] != -1:
                    mn = min(mn, ls[target - coin] + 1)
            if mn != float("inf"):
                ls[target] = mn
        print(ls)
        return ls[-1]
