from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, nums[0]

        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]


        return slow
