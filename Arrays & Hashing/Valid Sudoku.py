from typing import List
from collections import defaultdict


class Solution:
    def isValidSudokuThreeFor(self, board: List[List[str]]) -> bool:
        tset = set()
        for i in range(9):  # lines
            for j in range(9):
                if board[i][j] in tset:
                    print("false")
                    return False
                temp = board[i][j]
                if temp != ".":
                    tset.add(temp)
            tset.clear()

        for i in range(9):  # tables
            for j in range(9):
                if board[j][i] in tset:
                    return False
                temp = board[j][i]
                if temp != ".":
                    tset.add(temp)
            tset.clear()
        for i in range(9):  # squares
            for j in range(9):
                if board[j // 3 + (i // 3) * 3][j % 3 + (i % 3) * 3] in tset:
                    return False
                temp = board[j // 3 + (i // 3) * 3][j % 3 + (i % 3) * 3]
                if temp != ".":
                    tset.add(temp)
            tset.clear()
        return True

    def isValidSudokuOneFor(self, board: List[List[str]]) -> bool:
        ln = defaultdict(set)
        tb = defaultdict(set)
        sq = defaultdict(set)
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue
                if (value in ln[i] or
                        value in tb[j] or
                        value in sq[(i // 3, j // 3)]):
                    return False
                ln[i].add(value)
                tb[j].add(value)
                sq[(i // 3, j // 3)].add(value)

        return True
