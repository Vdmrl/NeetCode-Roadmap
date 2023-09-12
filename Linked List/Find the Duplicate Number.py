from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 532ms - 52%
        # 30.4mb - 98%
        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow_new = 0
        while slow != slow_new:
            slow, slow_new = nums[slow], nums[slow_new]
            if slow == slow_new:
                break
        return slow
