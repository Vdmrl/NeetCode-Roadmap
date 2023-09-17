# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # O(n) - 39ms - 96%
        # O(n) - 18.5mb - 92%
        return self.max_len_and_diam(root)[1]
    # [max_len, max_diam]
    def max_len_and_diam(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [0,0]
        left, right = self.max_len_and_diam(root.left), self.max_len_and_diam(root.right)
        return [1 + max(left[0], right[0]), max(left[1], right[1], left[0]+right[0])]