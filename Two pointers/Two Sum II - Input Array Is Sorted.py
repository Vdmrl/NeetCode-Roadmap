from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1
        while True:
            sm = numbers[lp] + numbers[rp]
            if sm > target:
                rp -= 1
            elif sm < target:
                lp += 1
            else:
                return [lp+1, rp+1]