from typing import List


class Solution:
    def search2LogN(self, nums: List[int], target: int) -> int:
        # log(n) + log(n)
        # pivot searching + search target with shift
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

    def searchLogN(self, nums: List[int], target: int) -> int:
        # 42ms 92%
        # 16.6mb 93%
        # log(n)
        # solution without pivot searching
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                if nums[left] > nums[mid] and target > nums[right]:  # left part
                    right = mid - 1
                else:  # right part
                    left = mid + 1
            elif target < nums[mid]:
                if nums[left] <= nums[mid] and target < nums[left]:  # left part
                    left = mid + 1
                else:  # right part
                    right = mid - 1
            else:
                return mid
        return -1

    def searchLogNUnd(self, nums: List[int], target: int) -> int:
        # 51ms 52%
        # 16.6mb 70%
        # log(n)
        # solution without pivot searching  (more understandable solution)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                if nums[left] <= nums[mid]:  # left part
                    left = mid + 1
                else:  # right part
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            elif target < nums[mid]:
                if nums[left] <= nums[mid]:  # left part
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:  # right part
                    right = mid - 1
            else:
                return mid
        return -1
