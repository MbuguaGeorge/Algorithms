class Node:
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node data: {self.data}"

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node