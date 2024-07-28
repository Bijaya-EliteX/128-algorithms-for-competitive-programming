class OurQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:
            # If out_stack is empty, reverse in_stack into out_stack
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()

# Create an instance of OurQueue
queue = OurQueue()

# Add elements to the queue
queue.push(10)
queue.push(20)
queue.push(30)

# Check the length of the queue
print(f"Length of queue: {len(queue)}")  # Output: 3

# Remove and print elements from the queue
print(queue.pop())  # Output: 10
print(queue.pop())  # Output: 20

# Add another element to the queue
queue.push(40)

# Check the length of the queue again
print(f"Length of queue: {len(queue)}")  # Output: 2

# Remove and print the remaining elements from the queue
print(queue.pop())  # Output: 30

print(f"the length of a queue:{len(queue)}")
