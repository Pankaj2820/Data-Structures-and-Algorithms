class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop(self):
        # Case 1: The list is empty
        if self.head is None:
            return None
        
        # Case 2: Only one node in the list
        if self.head.next is None:
            data = self.head.data
            del(self.head)
            self.head = None
            return data
        
        # Case 3: Multiple nodes
        # We need to find the second-to-last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # 'current' is now the second-to-last node
        last_node = current.next
        data = last_node.data
        
        current.next = None # Disconnect the last node
        del(last_node)      # Clean up memory
        
        return data

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        return f"<SinglyLinkedList: [{', '.join(nodes)}]>"
