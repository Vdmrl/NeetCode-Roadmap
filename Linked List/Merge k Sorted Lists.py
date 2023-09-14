from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n*log(k)) - 94ms - 73%
        # 19.9mb - 88ms
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            lst = []
            for i in range(0, len(lists), 2):
                lst.append(
                    self.mergeTwoLists(lists[i], lists[i + 1] if (i + 1) < len(lists) else None))
            lists = lst
        return lists[0]

    def mergeKListsBruteForce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n*k) - 6053ms - 5%
        # 19.7mb - 99%
        if not lists or len(lists) == 0:
            return None
        head = cur = ListNode()
        while True:
            min_ind = -1
            for i in range(1, len(lists)):
                if min_ind == -1 or lists[i] and lists[i].val < lists[min_ind].val:
                    min_ind = i
            if min_ind == -1:
                break
            cur.next = lists[min_ind]
            cur = cur.next
            lists[min_ind] = lists[min_ind].next
        return head

    def mergeKListsSort(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n*log(n)) 94ms - 73%
        # 20.4mb - 29%
        lst = []
        for i in lists:
            while i:
                lst.append(i.val)
                i = i.next
        if len(lst) == 0:
            return None
        lst.sort()
        head = ListNode(lst[0], None)
        cur = head
        for i in range(1, len(lst)):
            node = ListNode(lst[i])
            cur.next = node
            cur = node
        return head
