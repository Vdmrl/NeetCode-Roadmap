# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # O(n) - 180mx - 82%
        # O(n) - 34.9mb - 86%
        def countGood(root: TreeNode, mx: int = -1000000) -> int:
            l,r,m = 0,0,0
            if root.left:
                l = countGood(root.left, max(mx,root.val))
            if root.right:
                r = countGood(root.right, max(mx,root.val))
            if mx == -1000000 or root.val >= mx:
                m = 1
            return l + r + m
        return countGood(root)

