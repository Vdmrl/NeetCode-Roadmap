from typing import List, Set
from collections import defaultdict, Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(n * m * 4^n) - 1033ms - 92%
        # O(n) - 17.4mb - 5%
        used = set()
        cur_len: int = 0

        def dfs(i: int, j: int) -> bool:
            nonlocal cur_len
            if (cur_len >= len(word)
                    or i < 0
                    or i >= len(board)
                    or j < 0
                    or j >= len(board[0])
                    or board[i][j] != word[cur_len]
                    or tuple([i, j]) in used):  # del first
                return False
            cur_len += 1
            if cur_len == len(word):
                return True
            used.add(tuple([i, j]))
            if (dfs(i - 1, j)
                    or dfs(i + 1, j)
                    or dfs(i, j - 1)
                    or dfs(i, j + 1)):
                return True
            used.remove(tuple([i, j]))
            cur_len -= 1
            return False

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j):
                    return True

        return False
