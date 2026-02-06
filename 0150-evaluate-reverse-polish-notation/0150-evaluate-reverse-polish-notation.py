class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # using stack to calculate, iterate through stack:
        # 1. integer: push into stack
        # 2. operator: pop twice from stack, then calculate with operator, push result into stack
        # result: the last one integer in the stack

        def calculate(x, y, operator):
            if operator == '+':
                return x + y
            elif operator == '-':
                return x - y
            elif operator == '*':
                return x * y
            else:
                return int(x / y)

        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                result = calculate(x, y, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]

        
