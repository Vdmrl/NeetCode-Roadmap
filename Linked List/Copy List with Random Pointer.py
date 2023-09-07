from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # O(n)
        # 37ms 91%
        # 17.2 mb 93%
        ans_list, head_list = [], []
        thead, tans, ans = None, None, None
        if head:
            temp = Node(head.val)
            tans = temp
            ans_list.append(temp)
            head_list.append(head)
            ans = tans
            thead = head.next
        while thead:  # values
            temp = Node(thead.val)
            ans_list.append(temp)
            head_list.append(thead)
            tans.next = temp
            tans = tans.next
            thead = thead.next
        tans = ans
        while head:  # links
            tans.random = ans_list[head_list.index(head.random)]
            tans = tans.next
            head = head.next
        return ans
