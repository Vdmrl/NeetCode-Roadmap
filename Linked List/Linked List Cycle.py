from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) - 47ms - 97%
        # O(n) - 20.7mb - 15%
        cur = head
        st = set()
        while cur:
            if cur in st:
                return True
            st.add(cur)
            cur = cur.next
        return False

    def hasCycleFloydCicle(self, head: Optional[ListNode]) -> bool:
        # O(n) - 53ms - 85%
        # O(1) - 20.42mb - 68%
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
