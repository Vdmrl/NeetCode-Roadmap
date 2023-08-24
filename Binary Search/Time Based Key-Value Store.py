from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans, lst = "", self.dictionary[key]
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp > lst[mid][0]:
                ans = lst[mid][1]
                left = mid + 1
            elif timestamp < lst[mid][0]:
                right = mid - 1
            else:
                return lst[mid][1]
        return ans
