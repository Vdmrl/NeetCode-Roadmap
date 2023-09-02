from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n)
        # 31ms 99%
        # 19.9mb 73%
        prev = None
        curr = head
        while True:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            if curr.next == None:
                break
        return head
    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

