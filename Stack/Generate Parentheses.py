from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Solution without recursion
        # O(n^2)
        # 26ms 99.8%
        # 16.6mb 60%
        ans = [["(", n - 1, 1]]  # combination, number of available left and right parenthesis
        for i in range(n * 2 - 1):  # number of parenthesis - 1
            new_ans = []
            for j in range(len(ans)):
                temp = ans.pop()
                if temp[1] > 0:
                    new_ans.append([temp[0] + "(", temp[1] - 1, temp[2] + 1])
                if temp[2] > 0:
                    new_ans.append([temp[0] + ")", temp[1], temp[2] - 1])
            ans = new_ans
        new_ans = []
        for i in ans:
            new_ans.append(i[0])
        return new_ans

    def generateParenthesisRec(self, n: int) -> List[str]:
        # Solution with recursion
        # O(n^2)
        # 35ms 95%
        # 16.55mb 87%
        ans = []
        lst = []

        def generate(left: int, right: int) -> None:
            if left == 0 and right == 0:
                ans.append("".join(lst))
            if left > 0:
                lst.append("(")
                generate(left - 1, right + 1)
                lst.pop()
            if right > 0:
                lst.append(")")
                generate(left, right - 1)
                lst.pop()

        generate(n, 0)
        return ans
