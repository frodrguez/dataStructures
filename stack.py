# Stack:
# This data structure acts as the opposite of queues, as the last element imputed
# is the first to go out (LIFO - last in first out).

class Stack:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        self.elements.pop()

    def peek(self):
        if not self.is_empty():
            return self.elements[len(self.elements) - 1]

    def is_empty(self):
        return self.elements == []


# Testing:
if __name__ == '__main__':
    s = Stack()
    for idx in range(10):
        s.push(idx)
    print(s.peek())  # 9
    s.pop()  # bye 9
    s.pop()  # bye 8
    print(s.peek())  # 7
