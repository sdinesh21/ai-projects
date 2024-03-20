class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        """Return the top item from the stack without removing it."""
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

# Example usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Outputs: 3
print(s.peek()) # Outputs: 2
print(s.size()) # Outputs: 2