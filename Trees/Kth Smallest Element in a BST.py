# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # O(n) - 41ms - 98%
        # O(n) - 20.3mb - 96%
        def search(root, k, mn, n) -> List[int]:  # return [mn, n]
            if root.left:
                mn, n = search(root.left, k, mn, n)
            if n < k:
                mn, n = root.val, n + 1
            if root.right:
                mn, n = search(root.right, k, mn, n)
            return [mn, n]

        return search(root, k, -1, 0)[0]
