class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)
    
    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
    
    def peek(self):
        """Return the front item from the queue without removing it."""
        if self.is_empty():
            return None
        return self.queue[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Outputs: 1
print(q.peek())     # Outputs: 2
print(q.size())     # Outputs: 2