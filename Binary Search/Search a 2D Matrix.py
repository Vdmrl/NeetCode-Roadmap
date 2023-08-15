from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 40ms 99%
        # 16.7mb 87%
        t = 0
        b = len(matrix) - 1
        while t <= b:
            m = t + (b - t) // 2
            if matrix[m][-1] < target:
                t = m + 1
            elif matrix[m][0] > target:
                b = m - 1
            else:
                break
        if not (t <= b):
            return False

        l = 0
        r = len(matrix[m]) - 1
        while l <= r:
            с = l + (r - l) // 2
            if matrix[m][с] > target:
                r = с - 1
            elif matrix[m][с] < target:
                l = с + 1
            else:
                return True
        return False
