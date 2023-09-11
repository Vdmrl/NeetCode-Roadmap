from collections import deque


class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev, self.next = None, None


class LRUCache:
    # O(1) - 710ms - 65%
    # 0(1) - 78.5mb - 40%
    def __init__(self, capacity: int):
        self.key_to_val = dict()
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        self.capacity = capacity

    def delete(self, node: Node):
        prv, nxt = node.prev, node.next
        nxt.prev, prv.next = prv, nxt

    def append(self, node: Node):
        # append before right pointer from init
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, self.right

    def get(self, key: int) -> int:
        if key in self.key_to_val.keys():
            self.delete(self.key_to_val[key])
            self.append(self.key_to_val[key])
            return self.key_to_val[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val.keys():
            self.delete(self.key_to_val[key])
        self.key_to_val[key] = Node(key, value)
        self.append(self.key_to_val[key])
        if len(self.key_to_val) > self.capacity:
            del self.key_to_val[self.left.next.key]
            self.delete(self.left.next)
            pass
        return None
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
