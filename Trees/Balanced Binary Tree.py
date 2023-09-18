from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # O(n) - 44ms - 95%
        # O(n) - 21mb - 73%
        return self.is_balanced_and_lenght()[1]
    def is_balanced_and_lenght(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [0, True]
        left_len, left_b = self.is_balanced_and_lenght(root.left)
        right_len, right_b = self.is_balanced_and_lenght(root.right)
        return [max(left_len, right_len) + 1, left_b and right_b and abs(left_len - right_len) <= 1]
