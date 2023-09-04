from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[
        ListNode]:
        # Iterable solution
        # O(n + m)
        # 38ms 92%
        # 16.2mb 80%
        head, ans = None, None
        while list1 or list2:
            if not list2 or list1 and list1.val <= list2.val:
                if head == None:
                    head = list1
                    ans = head
                else:
                    head.next = list1
                    head = head.next
                list1 = list1.next
            else:
                if head == None:
                    head = list2
                    ans = head
                else:
                    head.next = list2
                    head = head.next
                list2 = list2.next
        return ans