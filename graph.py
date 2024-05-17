# Graph:
# A graph is a group of vertices connected between edges, forming a network of connected units. They can indeed
# represent a network of friendships in a social media, or cities connected via roads.
# They can be implemented with a list of neighbors for each vertex (which is done here) or with a matrix to represent weighted edges.
# The most important methods are the BFS (breadth first search) and DFS (depth first search), used to traverse through nodes in a graph.
# BFS: uses a queue to remember the order of incoming nodes. Prioritizes over nodes with fewer edges from the start to be checked-in first.
# DFS: uses a stack or recursion to backtrace effectively when it reaches a dead-end. Prioritizes over finding dead-ends, so it can backtrace and find more.

import queue
import stack

class vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)


class Graph:
    vertices = {}

    def add_vertex(self, v):
        if v not in self.vertices.values():
            self.vertices[v.value] = v

    def add_edge(self, u, v):
        if u in self.vertices.values() and v in self.vertices.values():
            u.add_neighbor(v)
            v.add_neighbor(u)

    @staticmethod
    def breadth_first_search(start):  # uses queue to implement
        nodes_values = []
        visited = []
        q = queue.Queue()
        q.enqueue(start)
        visited.append(start)
        while not q.is_empty():
            current_node = q.dequeue()
            nodes_values.append(current_node.value)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.append(neighbor)
        return nodes_values

    @staticmethod
    def depth_first_search(start):  # uses stack or recursion to implement
        nodes = []
        visited = []
        s = stack.Stack()
        s.push(start)
        visited.append(start)
        while not s.is_empty():
            nodes.append(s.peek())
            while s.peek() in nodes:
                for neighbor in s.peek().neighbors:
                    if neighbor not in visited:
                        s.push(neighbor)
                        visited.append(neighbor)
                        break
                if s.peek() in nodes:
                    s.pop()
        nodes_values = []
        for node in nodes:
            nodes_values.append(node.value)
        return nodes_values


# Testing:
graph = Graph()

node_1 = vertex(1)
node_2 = vertex(2)
node_3 = vertex(3)
node_4 = vertex(4)
node_5 = vertex(5)
node_6 = vertex(6)
node_7 = vertex(7)
node_8 = vertex(8)

graph.add_vertex(node_1)
graph.add_vertex(node_2)
graph.add_vertex(node_3)
graph.add_vertex(node_4)
graph.add_vertex(node_5)
graph.add_vertex(node_6)
graph.add_vertex(node_7)
graph.add_vertex(node_8)

graph.add_edge(node_1, node_3)
graph.add_edge(node_2, node_3)
graph.add_edge(node_3, node_4)
graph.add_edge(node_4, node_5)
graph.add_edge(node_2, node_5)
graph.add_edge(node_1, node_7)
graph.add_edge(node_7, node_4)
graph.add_edge(node_8, node_6)
graph.add_edge(node_2, node_6)

#  1---3---2---6
#  |   |   |   |
#  7---4---5   8
# BFS: starting at node 1, the first nodes encountered are its neighbors 3 and 7, then their neighbors 2 and 4, then 5 and 6 and finally 8.
# DFS: starting at node 1, finds all nodes in the closed loop 1,3,2,5,4,7 and then it backtraces until nodes 6 and 8 are discovered.
print(graph.breadth_first_search(node_1))  # [1, 3, 7, 2, 4, 5, 6, 8]
print(graph.depth_first_search(node_1))    # [1, 3, 2, 5, 4, 7, 6, 8]
