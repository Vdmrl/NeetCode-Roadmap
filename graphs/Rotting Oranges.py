from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0  # count fresh oranges
        rotten = []
        # find start rotten oranges
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    rotten.append((y, x))
                elif grid[y][x] == 1:
                    fresh += 1

        counter = 0
        while rotten:
            new_rotten = []
            for y, x in rotten:
                # rote all oranges around
                if y > 0 and grid[y - 1][x] == 1:
                    grid[y - 1][x] = 2
                    new_rotten.append((y - 1, x))
                    fresh -= 1
                if x > 0 and grid[y][x - 1] == 1:
                    grid[y][x - 1] = 2
                    new_rotten.append((y, x - 1))
                    fresh -= 1
                if y < len(grid) - 1 and grid[y + 1][x] == 1:
                    grid[y + 1][x] = 2
                    new_rotten.append((y + 1, x))
                    fresh -= 1
                if x < len(grid[0]) - 1 and grid[y][x + 1] == 1:
                    grid[y][x + 1] = 2
                    new_rotten.append((y, x + 1))
                    fresh -= 1
            if new_rotten:
                counter += 1
            rotten = new_rotten
        return counter if fresh == 0 else -1
