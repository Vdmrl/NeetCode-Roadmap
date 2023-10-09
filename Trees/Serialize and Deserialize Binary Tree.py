from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # O(n) - 89 - 98%
    # O(n) - 22mb - 98%
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        serialized = []

        def preorder(rt: Optional[TreeNode]) -> None:
            if not rt:
                serialized.append('N')
                return
            serialized.append(str(rt.val))
            preorder(rt.left)
            preorder(rt.right)

        preorder(root)
        return ";".join(serialized)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        dq = deque(data.split(';'))

        def ser() -> Optional[TreeNode]:
            p = dq.popleft()
            tree = TreeNode(int(p)) if p != "N" else None
            if tree:
                tree.left = ser()
                tree.right = ser()
            return tree

        return ser()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
