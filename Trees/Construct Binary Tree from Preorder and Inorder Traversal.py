from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(n) - 147ms - 64%
        # O(n) - 55.3mb - 69%
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        root.left = self.buildTree(preorder, inorder[:inorder.index(root.val)])
        root.right = self.buildTree(preorder, inorder[inorder.index(root.val)+1:])
        return root