from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(n*m) - 99%
        # O(n*m) - 70%
        pacific_mx: List[List[int]] = [[False for j in range(len(heights[0]))] for i in range(len(heights))]
        atlantic_mx: List[List[int]] = [[False for j in range(len(heights[0]))] for i in range(len(heights))]
        pointer = pacific_mx  # pointer to not pass pacific_mx in dfs function attributes

        def dfs(y: int, x: int) -> None:
            if pointer[y][x]:
                return
            pointer[y][x] = True
            if y > 0 and heights[y - 1][x] >= heights[y][x]:
                dfs(y - 1, x)
            if x > 0 and heights[y][x - 1] >= heights[y][x]:
                dfs(y, x - 1)
            if y < len(heights) - 1 and heights[y + 1][x] >= heights[y][x]:
                dfs(y + 1, x)
            if x < len(heights[0]) - 1 and heights[y][x + 1] >= heights[y][x]:
                dfs(y, x + 1)

        # top and left
        for i in range(len(heights[0])):
            dfs(0, i)
        for i in range(len(heights)):
            dfs(i, 0)

        # bottom and right
        pointer = atlantic_mx
        for i in range(len(heights[0])):
            dfs(len(heights) - 1, i)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1)

        ans = []
        for y in range(len(heights)):
            for x in range(len(heights[0])):
                if pacific_mx[y][x] and atlantic_mx[y][x]:
                    ans.append([y, x])
        return ans
