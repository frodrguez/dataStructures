# Generic tree:
# In the most generic form of a tree data structure, we can have any number of children in the nodes,
# and the tree's format is not relevant. There are no balancing operations neither.
# In this implementation I'll have, as usual, a separated class for the nodes. The Generic_Tree class will
# wrap it and build the parent/children relationships within new nodes added up via the add_node method.
# Other methods have been introduced to make it possible to print the tree in a more informative way.

class generic_node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.parent = None


class Generic_Tree:
    def __init__(self, root_node_value):
        root_node = generic_node(root_node_value)
        self.root = root_node

    def add_node(self, child_node):
        child_node.root.parent = self
        self.root.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.root.parent
        while p:
            level += 1
            p = p.root.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.root.parent else ""
        print(prefix + self.root.value)
        if len(self.root.children) > 0:
            for child in self.root.children:
                child.print_tree()


# Testing:
animals = Generic_Tree("animals")
mammals = Generic_Tree("mammals")
insects = Generic_Tree("insects")
birds = Generic_Tree("birds")
dog = Generic_Tree("dog")

mammals.add_node(Generic_Tree("horse"))
mammals.add_node(Generic_Tree("cow"))
mammals.add_node(dog)

birds.add_node(Generic_Tree("eagle"))
birds.add_node(Generic_Tree("condor"))

insects.add_node(Generic_Tree("fly"))
insects.add_node(Generic_Tree("bee"))

dog.add_node(Generic_Tree("Golden Retriever"))
dog.add_node(Generic_Tree("German Shepherd"))
dog.add_node(Generic_Tree("Siberian Husky"))

animals.add_node(mammals)
animals.add_node(insects)
animals.add_node(birds)

# Printing the tree:
animals.print_tree()

# animals
#     |__mammals
#         |__horse
#         |__cow
#         |__dog
#             |__Golden Retriever
#             |__German Shepherd
#             |__Siberian Husky
#     |__insects
#         |__fly
#         |__bee
#     |__birds
#         |__eagle
#         |__condor
