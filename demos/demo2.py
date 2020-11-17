"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.
As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.
The Stack class that you will use has been provided to you.
"""


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"


class QueueTwoStacks:
    def __init__(self):
        self.in_queue = Stack()
        self.out_queue = Stack()

    def enqueue(self, item):
        self.in_queue.push(item)

    def dequeue(self):
        if len(self.out_queue.data) == 0:
            while len(self.in_queue.data) > 0:
                newest_data = self.in_queue.pop()
                self.out_queue.push(newest_data)
            
            if len(self.out_queue.data) == 0:
                raise IndexError("Cannot dequeue from an empty queue!")
        
        return self.out_queue.pop()