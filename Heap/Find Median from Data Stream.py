import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        heapq.heapify(self.max_heap)  # left
        self.min_heap = []
        heapq.heapify(self.min_heap)  # right

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return
        if len(self.min_heap) == 1 and len(self.max_heap) == 1 and -self.max_heap[0] > self.min_heap[0]:
            self.max_heap[0], self.min_heap[0] = -self.min_heap[0], -self.max_heap[0]

        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) + 1 < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.min_heap) + 1 < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
