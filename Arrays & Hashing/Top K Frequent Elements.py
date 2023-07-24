from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def topKFrequentDict(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for number in nums:
            dic[number] += 1
        dic = sorted(dic, key=dic.get, reverse=True)
        return list(dic[0:k])

    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common(k)
        ans = []
        for i in count:
            ans.append(i[0])
        return ans
