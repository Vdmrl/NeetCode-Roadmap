# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # O(n) - 103ms - 72%
        # O(n) - 17.4mb - 75%
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 and not r2:
            return True
        if r1 and r2 and r1.val == r2.val:
            return True and self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)
        return False
