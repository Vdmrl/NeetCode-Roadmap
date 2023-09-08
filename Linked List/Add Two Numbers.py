# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 63ms 77%
        # 16.2mb 91%
        num_1, num_2 = [], []
        cur1, cur2 = l1, l2
        while cur1:
            num_1.append(str(cur1.val))
            cur1 = cur1.next
        while cur2:
            num_2.append(str(cur2.val))
            cur2 = cur2.next
        num_1 = "".join(reversed(num_1))
        num_2 = "".join(reversed(num_2))
        sm = int(num_1) + int(num_2)
        head, temp = None, None
        for i in str(sm):
            temp = ListNode(int(i), head)
            head = temp
        return temp
