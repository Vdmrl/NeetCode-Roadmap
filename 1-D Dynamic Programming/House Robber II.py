from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob1(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            nums[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            return max(nums[-1], nums[-2])

        return max(rob1(nums[1:]), rob1(nums[:-1]))