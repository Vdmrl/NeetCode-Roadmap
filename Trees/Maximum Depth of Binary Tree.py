from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRec(self, root: Optional[TreeNode]) -> int:
        # O(n) - 41ms - 88%
        # O(n) - 18.6mb - 76%
        if not root:
            return 0
        return 1 + max(self.maxDepthRec(root.left), self.maxDepthRec(root.right))

    def maxDepthIter(self, root: Optional[TreeNode]) -> int:
        # O(n) - 45ms - 70%
        # O(n) - 18.6mb - 90%
        ans = 0
        dq = deque([(root, 1)])
        while dq:
            node, depth = dq.popleft()
            if node:
                ans = max(ans, depth)
                dq.append((node.left, depth + 1))
                dq.append((node.right, depth + 1))
        return ans
