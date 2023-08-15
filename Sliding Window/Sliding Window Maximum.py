class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1287ms 97%
        # 33.2 mb 42%
        if k == 1:
            return nums
        l = 0
        ans = []
        dq = deque()
        for r in range(0,len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if l > dq[0]:
                dq.popleft()
            if r+1 >= k:
                ans.append(nums[dq[0]])
                l += 1
        return ans