from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # O(n) - 35ms - 86%
        # O(n) - 15.97mb - 99.9%
        if not root:
            return None
        dq = deque()
        dq.append(root)
        ans = []
        while dq:
            ans.append(dq[-1].val)
            for i in range(len(dq)):
                rt = dq.popleft()
                if rt.left:
                    dq.append(rt.left)
                if rt.right:
                    dq.append(rt.right)
        return ans

