class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.hashmap = {}
        
    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False

        self.hashmap[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False

        idx = self.hashmap[val]
        last = self.vals[-1]

        self.vals[idx] = last
        self.vals.pop()
        
        self.hashmap[last] = idx  
        del self.hashmap[val]  
        # delete must be last, in case the last one to be removed

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()