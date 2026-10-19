class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q1:
            return None

        n = len(self.q1)
        for _ in range(n - 1):
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()

        while self.q2:
            self.q1.append(self.q2.popleft())
        return res
        
    def top(self) -> int:
        if not self.q1:
            return None

        n = len(self.q1)
        for _ in range(n - 1):
            self.q2.append(self.q1.popleft())
        res = self.q1[0]

        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q1.append(self.q1.popleft())
        return res

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()