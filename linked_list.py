"""
Run the file as "python3 -i linked_list.py" to enter the python terminal
Now try out the methods defined in the classes

"""

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

    """
    Function is_empty() checks whether the head Node is 
    empty and evaluates to True if it is.
    """
    def is_empty(self) -> bool:
        return self.head == None

    """
    Function size() keeps track of current (a local variable) 
    and increments count while traversing the List.
    """
    def size(self):
        current = self.head
        count = 0

        while current is not None: # While we are not at the tail
            count += 1
            current = current.next_node

        return count

    """
    Function add() adds a new Node at head.
    """
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head # New Node is set as Head 
        self.head = new_node           # while keeping track of the old Head

    """
    Function search() traverse the List till a value is found.
    """
    def search(self, val):
        current = self.head

        while current is not None:
            if current.data == val:
                return current
            else:
                current = current.next_node
        return None

    """
    A string representation of the Linked List
    """
    def __repr__(self):
        nodes = []
        current = self.head # current is set as Head

        while current is not None: # while we are not at the tail.
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return '-> '.join(nodes)
