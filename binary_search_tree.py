# Binary search tree:
# This data structure is helpful for arranging elements in a tree such that each node contains at most 2 children. The left child is smaller
# than its parent while the right child is greater. In this implementation I only used one class that will symbolize the node unit. To construct
# the tree in the final testing, the root must be called as to construct the class, while the other nodes will be treated by the add_node method.
# A ot of recursion happens within the methods, as they compare the needed values and recall the same method in the left or right child.
# Tree traversals also have been implemented and compared in the final testing.

# Time complexity analysis: search/insert/delete operations will have the best scenario of O(log n), that happens
# when the tree is balanced. Worst case scenario will correspond to a complete skewed tree and the complexity will be O(n).

# It is clear that balancing maneuvers are very important to the efficiency of a tree. They will be studied in the AVL-tree, as well with the deletion method.

class Binary_Search_Tree_Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def add_node(self, value):  # we'll call this method from the root node (the one that constructed the tree. So always starts at the root!)
        if value == self.value:
            return
        elif value > self.value:
            if self.right_child is None:
                self.right_child = Binary_Search_Tree_Node(value)
            else:
                self.right_child.add_node(value)
        elif value < self.value:
            if self.left_child is None:
                self.left_child = Binary_Search_Tree_Node(value)
            else:
                self.left_child.add_node(value)

    def search_node(self, value):  # we'll call this method from the root node (the one that constructed the tree. So always starts at the root!)
        if value == self.value:
            return True
        elif value > self.value:
            if self.right_child is None:
                return False
            else:
                return self.right_child.search_node(value)
        elif value < self.value:
            if self.left_child is None:
                return False
            else:
                return self.left_child.search_node(value)

    def inorder_traversal(self):
        elements = []
        if self.left_child is not None:
            elements += self.left_child.inorder_traversal()    # 1st: recursively on left subtree
        elements.append(self.value)                            # 2nd: current node
        if self.right_child is not None:
            elements += self.right_child.inorder_traversal()   # 3rd: recursively on right subtree
        return elements

    def preorder_traversal(self):
        elements = [self.value]                                # 1st: current node
        if self.left_child is not None:
            elements += self.left_child.preorder_traversal()   # 2nd: recursively on left subtree
        if self.right_child is not None:
            elements += self.right_child.preorder_traversal()  # 3rd: recursively on right subtree
        return elements

    def postorder_traversal(self):
        elements = []
        if self.left_child is not None:
            elements += self.left_child.postorder_traversal()   # 1st: recursively on left subtree
        if self.right_child is not None:
            elements += self.right_child.postorder_traversal()  # 2nd: recursively on right subtree
        elements.append(self.value)                             # 3rd: current node
        return elements


# Testing:
root = Binary_Search_Tree_Node(40)
root.add_node(19)
root.add_node(43)
root.add_node(8)
root.add_node(13)
root.add_node(27)
root.add_node(27)
root.add_node(22)
root.add_node(25)
root.add_node(34)

#             40
#           /    \
#         19     43
#        /  \
#      8     27
#      \     /  \
#       13  22   34
#            \
#             25

print(root.search_node(90))  # False
print(root.search_node(8))   # True

print(root.inorder_traversal())    # [8, 13, 19, 22, 25, 27, 34, 40, 43] (ascending order)
print(root.preorder_traversal())   # [40, 19, 8, 13, 27, 22, 25, 34, 43] (starts at root and goes straight to smallest leaves)
print(root.postorder_traversal())  # [13, 8, 25, 22, 34, 27, 19, 43, 40] (starts at smallest leaf and goes up, or down if find more leaves)
