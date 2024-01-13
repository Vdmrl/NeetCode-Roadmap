from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()  # column
        pos_diag = set()  # row + column
        neg_diag = set()  # row - column
        solutions = []
        cur_solution = []

        def backtracking(row: int) -> None:
            if row >= n:  # right solution
                solutions.append(cur_solution.copy())

            for c in range(n):
                if c not in col and (row + c) not in pos_diag and (row - c) not in neg_diag:  # chech for intersections
                    # place queen
                    # and add it intersections
                    pos_diag.add(row + c)
                    neg_diag.add(row - c)
                    col.add(c)

                    # add new current solution row
                    line = ["." for i in range(n)]
                    line[c] = "Q"
                    cur_solution.append("".join(line))

                    backtracking(row + 1)  # recursion

                    # delete previous row
                    cur_solution.pop()

                    # delete previous intersections
                    pos_diag.remove(row + c)
                    neg_diag.remove(row - c)
                    col.remove(c)

        backtracking(0)
        return solutions
