from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n)
        # 35ms 92%
        # 16.1mb 93%
        temp = head
        ln = 0
        while temp:  # count length
            ln += 1
            temp = temp.next
        n = ln - n
        if n == 0:  # del first element
            head = head.next
            return head
        # del not first element
        ind = 1
        temp = head
        while ind != n:  # find note before note for delete
            temp = temp.next
            ind += 1
        temp.next = temp.next.next  # delete node
        return head

    def removeNthFromEndTwoPointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n)
        # 32ms 96%
        # 16.29mb 70%
        temp = ListNode(None, head)  # Create a new list with a dummy node before the head.
        left, right = temp, head
        for i in range(n):  # Move 'right' pointer n nodes to the right.
            right = right.next
        while right:  # Move 'left' and 'right' pointers until 'right' reaches the end.
            left = left.next
            right = right.next
        left.next = left.next.next  # delete nth node
        # return "temp.next" because old list (head) would return the deleted node
        # if it were necessary to delete first node (it is still have links to all list
        # because it wasn't deleted, but do not have link to it)
        return temp.next
