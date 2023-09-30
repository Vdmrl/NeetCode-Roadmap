from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(n) - 38ms - 91%
        # O(n) - 17mb - 82.8%
        if not root:
            return []
        ans = [[]]
        nodes = [root]
        new_nodes = []
        while nodes:
            while nodes:
                rt = nodes.pop(0)
                ans[-1].append(rt.val)
                if rt.left:
                    new_nodes.append(rt.left)
                if rt.right:
                    new_nodes.append(rt.right)
            if new_nodes:
                nodes = new_nodes
                new_nodes = []
                ans.append([])
        return ans
