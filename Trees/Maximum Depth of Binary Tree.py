from typing import Optional
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
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
