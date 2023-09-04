from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterable solution
        # O(n)
        # 31ms 99%
        # 19.9mb 73%
        if head is None or head.next == None:
            return head
        prev, curr = None, head
        while True:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            if curr.next == None:
                curr.next = prev
                break
        return curr

    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution
        # O(n)
        # 40ms 82%
        # 22.78mb 13%
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseListRec(head.next)
            head.next.next = head
        head.next = None

        return new_head
