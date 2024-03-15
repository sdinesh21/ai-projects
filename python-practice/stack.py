class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Example usage
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Returns -3
minStack.pop()
print(minStack.top())     # Returns 0
print(minStack.getMin())  # Returns -2