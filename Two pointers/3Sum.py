from typing import List
from collections import defaultdict


class Solution:
    def threeSumNoSort(self, nums: List[int]) -> List[List[int]]:
        # 4286 ms
        # 25 mb
        ans = []
        checked = set()
        for i in range(len(nums)):  # n
            if nums[i] in checked:
                continue
            checked.add(nums[i])
            # two sum
            target = -nums[i]
            dic = defaultdict(int)
            for j in range(len(nums)):  # n**2
                if j == i:
                    continue
                difference = target - nums[j]
                if nums[j] in dic.keys():
                    ans.append([nums[i], nums[j], dic[nums[j]]])
                dic[difference] = nums[j]
        # delete duplicates
        st = set()
        for i in ans:
            st.add(tuple(sorted(i)))
        ans = []
        for i in st:
            ans.append(list(i))
        return ans

    def threeSumSort(self, nums: List[int]) -> List[List[int]]:
        # 709 ms
        # 21 mb
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if nums[i-1] == nums[i] and i != 0:
                continue
            target = -nums[i]
            lp, rp = i + 1, len(nums) - 1
            while lp < rp:
                sm = nums[lp] + nums[rp]
                if sm == target:
                    ans.append([-target, nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    while nums[lp-1] == nums[lp] and lp < rp:
                        lp += 1
                elif sm > target:
                    rp -= 1
                else:
                    lp += 1
        return ans
