# Linked list:
# In a linked list, the nodes within keep a pointer to the next node. Thus, accessing an element has complexity O(n),
# as it needs to traverse nodes until the desired one. However, adding/removing elements has complexity O(1).
# This behaviour contrasts with the one from arrays, which has O(n) for adding/removing (sequential) and O(1) for accessing (direct).
# The implementation will contain a subclass called linked_list_node, that the user won't have access and will be wrapped by the main class.

class linked_list_node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self):
        self.first_node = linked_list_node()

    def __repr__(self):
        elements = []
        cur_node = self.first_node
        while cur_node:
            elements.append(cur_node.value)
            cur_node = cur_node.next
        elements.pop(0)
        return str(elements)

    def length(self):
        cur_node = self.first_node
        size = 0
        while cur_node.next != None:
            size += 1
            cur_node = cur_node.next
        return size

    def last_node(self):
        last = self.first_node
        while last.next != None:
            last = last.next
        return last

    def insert(self, data):
        new_node = linked_list_node(data)
        self.last_node().next = new_node

    def delete(self, index):
        cur_node = self.first_node.next
        prev_node = cur_node
        if index == 0:
            self.first_node.next = cur_node.next
        else:
            for i in range(0, index):
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = cur_node.next

    def get(self, index):
        if index >= self.length():
            print("Failed to access index greater than list's size.")
            return None
        else:
            node = self.first_node.next
            for i in range(0, index):
                node = node.next
            return node.value


# Testing:
l = Linked_list()
l.insert(0)
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
print(l)  # [0, 1, 2, 3, 4]
print("Element at first index: %d" % l.get(0))  # Element at first index: 0
print(l.length())  # 5
l.delete(4)
print(l)  # [0, 1, 2, 3]
