class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        n = len(self.q)
        for _ in range(n - 1):
            self.q.append(self.q.popleft())
        res = self.q.popleft()
        return res
        
    def top(self) -> int:
        n = len(self.q)
        for _ in range(n - 1):
            self.q.append(self.q.popleft())
        res = self.q[0]
        self.q.append(self.q.popleft())
        return res

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()