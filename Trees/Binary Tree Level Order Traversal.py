from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(n) - 38ms - 91%
        # O(n) - 17mb - 82.8%
        if not root:
            return []
        ans = [[]]
        nodes = deque(root)
        while nodes:
            for i in range(len(nodes)):
                rt = nodes.popleft()
                ans[-1].append(rt.val)
                if rt.left:
                    nodes.append(rt.left)
                if rt.right:
                    nodes.append(rt.right)
            if nodes:
                ans.append([])
        return ans
