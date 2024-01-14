from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(n*logn) - timsort
        # O(n) - Timsort
        # sort by distance and slice k min points
        return sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5)[:k]
