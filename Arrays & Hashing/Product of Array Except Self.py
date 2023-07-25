from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        ans = []

        pr = 1
        for i in range(0, ln):
            ans.append(pr)
            pr *= nums[i]
        pt = 1
        for i in range(1,ln+1):
            ans[-i] *= pt
            pt *= nums[-i]
        return ans
s = Solution().productExceptSelf([1,2,3,4])
