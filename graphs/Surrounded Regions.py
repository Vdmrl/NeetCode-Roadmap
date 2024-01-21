from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # deep copy with filling all initial board with "X"
        board_copy = [["X" for i in range(len(board[0]))] for i in range(len(board))]
        for y in range(len(board)):
            for x in range(len(board[0])):
                board_copy[y][x] = board[y][x]
                board[y][x] = "X"

        def dfs(y: int, x: int) -> None:
            """
                place "0" in board if board_copy have "0" in the same place
            """
            if board_copy[y][x] == "X":
                return
            board_copy[y][x] = "X"
            board[y][x] = "O"
            if y > 0:
                dfs(y - 1, x)
            if x > 0:
                dfs(y, x - 1)
            if y < len(board_copy) - 1:
                dfs(y + 1, x)
            if x < len(board_copy[0]) - 1:
                dfs(y, x + 1)

        # place "0" on borders
        for i in range(len(board_copy[0])):
            dfs(0, i)
            dfs(len(board_copy) - 1, i)
        for i in range(len(board_copy)):
            dfs(i, 0)
            dfs(i, len(board_copy[0]) - 1)
