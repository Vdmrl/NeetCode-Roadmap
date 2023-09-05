from collections import deque
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderListLst(self, head: Optional[ListNode]) -> None:
        # O(n)
        # 66ms 98%
        # 27.2mb 35%
        left, right = list(), list()
        while head:
            left.append(head)
            head = head.next
        right = left[(len(left) + 1) // 2:]
        del left[(len(left) + 1) // 2:]
        left.reverse()
        head = left.pop()
        temp = head
        while right:
            # add right
            r = right.pop()
            r.next = None
            temp.next = r
            temp = temp.next
            # add left
            if left:
                l = left.pop()
                l.next = None
                temp.next = l
                temp = temp.next
    def reorderListDeq(self, head: Optional[ListNode]) -> None:
        # O(n)
        # 76ms 82%
        # 26mb 87%
        deq = deque()
        while head:
            deq.append(head)
            head = head.next
        head = deq.popleft()
        temp = head
        while deq:
            # add right
            r = deq.pop()
            r.next = None
            temp.next = r
            temp = temp.next
            # add left
            if deq:
                l = deq.popleft()
                l.next = None
                temp.next = l
                temp = temp.next



