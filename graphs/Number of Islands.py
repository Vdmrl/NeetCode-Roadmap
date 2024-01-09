from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs_zer(posy: int, posx: int) -> None:
            if grid[posy][posx] == "1":
                grid[posy][posx] = "0"
                if posy + 1 < len(grid):
                    dfs_zer(posy + 1, posx)
                if posy - 1 >= 0:
                    dfs_zer(posy - 1, posx)
                if posx + 1 < len(grid[0]):
                    dfs_zer(posy, posx + 1)
                if posx - 1 >= 0:
                    dfs_zer(posy, posx - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs_zer(i,j)
        return count

