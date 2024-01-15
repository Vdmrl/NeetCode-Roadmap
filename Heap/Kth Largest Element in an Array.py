from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap
        # O(n + k*log(n))
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

        # quick select
        # O(n) - mid
        # O(n**2) - worst
        # Time limit on last testcase
        #def partition(left: int, right: int) -> int:
        #    for i in range(left, right):
        #        if nums[i] <= nums[right]:
        #            nums[left], nums[i] = nums[i], nums[left]
        #            left += 1
        #    nums[left], nums[right] = nums[right], nums[left]
        #    return left
        #k = len(nums) - k
        #left, right = 0, len(nums) - 1
        #while left < right:
        #    pivot = partition(left,right)
        #    if pivot < k:
        #        left += 1
        #    elif pivot > k:
        #        right -= 1
        #    else:
        #        break
        #return nums[k]
