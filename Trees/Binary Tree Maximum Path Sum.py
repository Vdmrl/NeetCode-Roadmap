from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # O(n) - 65ms - 98%
        # O(n) - 23.9mb - 40%
        def maxPath(root: Optional[TreeNode]) -> List[int]:  # [one_max, two_max]
            if not root:
                return [-10000, -10000]
            if not root.left and not root.right:
                return [root.val, root.val]
            left_one_max, left_two_max = maxPath(root.left)
            right_one_max, right_two_max = maxPath(root.right)
            return [max(0, left_one_max, right_one_max) + root.val,
                    max(left_two_max, right_two_max, left_one_max + root.val + right_one_max,
                        left_one_max + root.val, root.val + right_one_max, root.val)]

        return maxPath(root)[1]
