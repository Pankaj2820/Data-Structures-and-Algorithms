class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, index):
        # ERROR HANDLING: Must raise ValueError for ANY out-of-bounds index
        # This includes index 0 if the list is empty (size is 0)
        if index < 0 or index >= self.size:
            raise ValueError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        
        data = current.data

        # Update the 'next' pointer of the PREVIOUS node
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next # Removing the head
            
        # Update the 'prev' pointer of the NEXT node
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev # Removing the tail

        self.size -= 1
        return data

    def __repr__(self):
        # Strictly matches: <DoublyLinkedList (X elements): [a, b]>
        nodes = [str(curr.data) for curr in self._get_nodes()]
        return f"<DoublyLinkedList ({self.size} elements): [{', '.join(nodes)}]>"

    def _get_nodes(self):
        """Helper to yield nodes for repr."""
        curr = self.head
        while curr:
            yield curr
            curr = curr.next