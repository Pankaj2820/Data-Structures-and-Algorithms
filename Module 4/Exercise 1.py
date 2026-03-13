class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, data):
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if not self._top:
            return None
        popped_node = self._top
        self._top = self._top.next
        self._size -= 1
        return popped_node.data

    def __repr__(self):
        elements = []
        current = self._top
        while current:
            elements.append(str(current.data))
            current = current.next
        
        label = "element" if self._size == 1 else "elements"
        return f"<Stack ({self._size} {label}): [{', '.join(elements)}]>"


if __name__ == "__main__":
    mystack = Stack()
    mystack.push('A')
    mystack.push('B')
    mystack.push('C')