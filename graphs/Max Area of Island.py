from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs_size(posy: int, posx: int) -> int:
            size = 0
            if grid[posy][posx] == 1:
                size += 1
                grid[posy][posx] = 0
                if posy + 1 < len(grid):
                    size += dfs_size(posy + 1, posx)
                if posy - 1 >= 0:
                    size += dfs_size(posy - 1, posx)
                if posx + 1 < len(grid[0]):
                    size += dfs_size(posy, posx + 1)
                if posx - 1 >= 0:
                    size += dfs_size(posy, posx - 1)
            return size

        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    mx = max(mx, dfs_size(i, j))
        return mx
