class ListNode:
    def __init__(self, count=1, keys=None, prev=None, nxt=None):
        self.count = count
        self.keys = set() if keys is None else keys
        self.prev = prev
        self.nxt = nxt

class AllOne:

    def __init__(self):
        self.hashmap = {} # str: node
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.nxt = self.tail   # small -> big
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.hashmap:
            if self.head.nxt.count == 1:
                self.head.nxt.keys.add(key)
                self.hashmap[key] = self.head.nxt
            else:
                new = ListNode()
                new.keys.add(key)
                self.add(new, self.head)
                self.hashmap[key] = new

        else:
            curr = self.hashmap[key]
            curr.keys.remove(key)
            if curr.nxt.count == curr.count + 1:
                curr.nxt.keys.add(key)
                self.hashmap[key] = curr.nxt
            else:
                new = ListNode()
                new.count = curr.count + 1
                new.keys.add(key)
                self.add(new, curr)
                self.hashmap[key] = new

            if not curr.keys:
                self.remove(curr)


    def dec(self, key: str) -> None:
        curr = self.hashmap[key]
        curr.keys.remove(key)
        if curr.count == 1:
            del self.hashmap[key]
        else:
            if curr.prev.count == curr.count - 1:
                curr.prev.keys.add(key)
                self.hashmap[key] = curr.prev
            else:
                new = ListNode()
                new.count = curr.count - 1
                new.keys.add(key)
                self.add(new, curr.prev)
                self.hashmap[key] = new

        if not curr.keys:
            self.remove(curr)

    def getMaxKey(self) -> str:
        return '' if not self.hashmap else next(iter(self.tail.prev.keys))
        
    def getMinKey(self) -> str:
        return '' if not self.hashmap else next(iter(self.head.nxt.keys))

    def add(self, node, anchor) -> None:
        node.nxt = anchor.nxt
        anchor.nxt.prev = node
        anchor.nxt = node
        node.prev = anchor

    def remove(self, node) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        node.prev = None
        node.nxt = None

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()