# Deque:
# A deque is a data structure very similar to the queue.
# The difference's it is possible to insert/remove in both ways (it stands for "double ended queue").
# Similar methods from the Queue class have been implemented, and another useful ones.
# The __str__ method allows us to wrap the print function, without needing to access elements outside the class.

class Deque:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def enqueue_left(self, value):
        self.elements.insert(0, value)

    def enqueue_right(self, value):
        self.elements.append(value)

    def dequeue_left(self):
        self.elements.pop(0)

    def dequeue_right(self):
        self.elements.pop()

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def clear(self):
        self.elements = []


# Testing:
d = Deque()
for idx in range(5):
    d.enqueue_left(idx)
print(d)  # [4, 3, 2, 1, 0]
d.dequeue_right()
print(d)  # [4, 3, 2, 1]
d.clear()
for idx in range(5):
    d.enqueue_right(idx)
print(d)  # [0, 1, 2, 3, 4]
d.dequeue_left()
print(d)  # [1, 2, 3, 4]
