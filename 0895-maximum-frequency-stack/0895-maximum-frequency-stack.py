class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        if self.freq[val] > self.maxfreq:
            self.maxfreq = self.freq[val]

    def pop(self) -> int:
        target = self.group[self.maxfreq].pop()
        self.freq[target] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return target

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()