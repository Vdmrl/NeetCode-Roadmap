from typing import List


class Solution:
    def search2LogN(self, nums: List[int], target: int) -> int:
        # log(n) + log(n)
        # 37ms 98%
        # 16.5mb 93%
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        swap = len(nums) - right
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[(mid - swap) % len(nums)]:
                left = mid + 1
            elif target < nums[(mid - swap) % len(nums)]:
                right = mid - 1
            else:
                return (mid - swap) % len(nums)
        return -1
