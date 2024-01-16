from typing import List
from collections import deque  # for queue
from collections import Counter  # to count commands
import heapq  # for max heap


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:  # edge case
            return len(tasks)
        # tasks to max heap with amounts
        tasks = Counter(tasks)
        tasks = [-v for v in tasks.values()]
        heapq.heapify(tasks)
        # queue for amount with activation time pairs
        queue = deque()
        timer = 0
        while tasks or queue:
            timer += 1

            # check queue every tick
            if queue and timer > queue[0][1]:
                heapq.heappush(tasks, queue.popleft()[0])

            # check tasks every turn
            if tasks:
                amount = heapq.heappop(tasks) + 1
                if amount < 0:
                    queue.append([amount, timer + n])

        return timer
