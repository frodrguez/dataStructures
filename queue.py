# Queue:
# It is a storage of elements that holds them in order, and pop them out in the order they got there (FIFO - first in fist out).
# So basic methods of this class would be enqueue, dequeue, and peek, to see the next element to get out.

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        self.elements.pop(0)

    def peek(self):
        return self.elements[0]


# Testing:
q = Queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)

print(q.peek())  # [7,8,9,10], so it prints 7
q.dequeue()      # 7 <--[8,9,10]
print(q.peek())  # [8,9,10], so it prints 8
