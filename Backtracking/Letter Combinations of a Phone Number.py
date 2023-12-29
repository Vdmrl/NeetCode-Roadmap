from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(n**3) - 35ms - 76%
        # O(n**3) - 17.1 mb - 13%
        # st = {"2", "3", "4", "5", "6", "7", "8", "9"}
        # digits = "".join(filter(lambda x: x in st, digits))
        dc = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
              "9": "wxyz"}
        ans = [""] if digits else []

        for digit in digits:
            new = []
            for i in ans:
                for j in dc[digit]:
                    new.append(i + j)
            ans = new
        return ans


print(Solution().letterCombinations("23"))
