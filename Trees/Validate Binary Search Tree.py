from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # O(n) - 48ms - 57%
        # O(n) - 18.3mb - 99.9%
        def isValid(root: Optional[TreeNode], mn=float('-inf'), mx=float('+inf')) -> bool:
            if not root:
                return True
            if not (mn < root.val < mx):
                return False
            return isValid(root.left, mn, root.val) and isValid(root.right, root.val, mx)
        return isValid(root)
