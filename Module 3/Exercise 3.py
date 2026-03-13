class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of bounds")

        if index == 0:
            removed_node = self.head
            data = removed_node.data
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return data

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        
        removed_node = prev.next
        data = removed_node.data
        prev.next = removed_node.next
        
        if index == self.size - 1:
            self.tail = prev
            
        self.size -= 1
        return data

    def __repr__(self):
        # Ensure the formatting here matches the expected string exactly
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        return f"<SinglyLinkedList ({self.size} elements): [{', '.join(nodes)}]>"