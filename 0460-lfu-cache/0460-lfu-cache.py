class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)


    def _update_freq(self, key):
        freq = self.key_to_freq[key]
        self.key_to_freq[key] += 1

        del self.freq_to_keys[freq][key] # delete before if check
        if self.min_freq == freq and not self.freq_to_keys[freq]:
            self.min_freq += 1
        
        self.freq_to_keys[freq + 1][key] = True  
        

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self._update_freq(key)
        return self.key_to_val[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.cap:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = True
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)