from collections import deque, defaultdict
import heapq
from typing import List


class Twitter:
    RECENT_AMOUNT = 10

    def __init__(self):
        self.counter = 0
        self.subscriptions = defaultdict(set)
        self.posts = defaultdict(deque)  # for stack

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft([-self.counter, tweetId])
        self.counter += 1
        # pop explicit posts
        while len(self.posts[userId]) > self.RECENT_AMOUNT:
            self.posts[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        # form min heap from all posts
        hq = []
        for i in self.subscriptions[userId]:
            if temp:=self.posts[i]:
                hq.append(temp.copy())
        if temp:=self.posts[userId]:
                hq.append(temp.copy())
        heapq.heapify(hq)

        # get last 10 posts
        ls = []
        while hq and len(ls) < 10:
            last = heapq.heappop(hq)
            ls.append(last.popleft()[1])
            if last:
                heapq.heappush(hq, last)
        return ls

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.subscriptions:
            self.subscriptions[followerId].remove(followeeId)