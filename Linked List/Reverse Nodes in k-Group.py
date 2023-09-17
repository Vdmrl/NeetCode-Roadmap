# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) - 45ms - 93%
        # O(1) - 17.36mb - 90%
        dummy_node = prev_node = ListNode(0, head)
        while True:
            kth = self.findKth(prev_node, k)
            next_node = kth.next
            if not kth:
                break
            prev, curr = kth.next, prev_node.next
            while curr != next_node:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = prev_node.next
            prev_node.next = kth
            prev_node = temp
        return dummy_node.next

    def findKth(self, head: Optional[ListNode], k: int):
        count = 0
        while head:
            count += 1
            head = head.next
        return head
