from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 92ms 74%
        # 16.4mb 99%
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) < len(nums2):  # nums1 always longer than nums2
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums2) - 1
        while True:
            mid2 = (left + right) // 2
            mid1 = half - mid2 - 2

            min1 = nums1[mid1] if mid1 >= 0 else float("-infinity")
            min2 = nums2[mid2] if mid2 >= 0 else float("-infinity")
            max1 = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float("infinity")
            max2 = nums2[mid2 + 1] if (mid2 + 1) < len(nums2) else float("infinity")

            if (min1 <= max2) and (min2 <= max1):
                # odd
                if len(total) % 2:
                    return min(min1,min2)
                # even
                return (max(min1,min2) + min(max1, max2)) / 2
            elif min1 > max2:
                left = mid2 + 1
            else:
                right = mid1 - 1

