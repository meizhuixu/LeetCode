class ListNode:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.add(node)

        else:
            new = ListNode(key, value)
            self.hashmap[key] = new
            self.add(new)
            
            if len(self.hashmap) > self.cap:
                remove_node = self.head.nxt
                del self.hashmap[remove_node.key]
                self.remove(remove_node)

    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        node.prev = None
        node.nxt = None

    def add(self, node):
        self.tail.prev.nxt = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.nxt = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)