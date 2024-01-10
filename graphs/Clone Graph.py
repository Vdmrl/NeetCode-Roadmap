# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dc = dict()

        # Copy all nodes into dictionary
        def hash(nd: Optional['Node']) -> None:
            if nd.val not in dc.keys():
                dc[nd.val] = Node(nd.val)
                for neighbor in nd.neighbors:
                    if neighbor.val not in dc.keys():
                        hash(neighbor)



        def clone(nd: Optional['Node']) -> None:
            if not dc[nd.val].neighbors:
                new_neighbors = []
                for neighbor in nd.neighbors:
                    new_neighbors.append(dc[neighbor.val])
                dc[nd.val].neighbors = new_neighbors
                for neighbor in nd.neighbors:
                    clone(neighbor)

        hash(node)
        clone(node)
        return dc[node.val]