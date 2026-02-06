class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if self.stack2:
            self.stack2.append(min(self.stack2[-1], val))
        else:
            self.stack2.append(val)
        

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()