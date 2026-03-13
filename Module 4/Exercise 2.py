class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

def check_balance(text):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    opens = set('([{')
    closes = set(')]}')
    count = 0

    for i, ch in enumerate(text):
        if ch in opens:
            stack.push((ch, i))
        elif ch in closes:
            # Check if stack is empty before popping
            if stack.size() == 0:
                return f"Match error at position {i}"
            
            # Pop returns a tuple: (char, index)
            top, _ = stack.pop()
            
            if top != pairs[ch]:
                return f"Match error at position {i}"
            count += 1

    # Check for unclosed opening brackets
    if stack.size() > 0:
        _, pos = stack.pop()
        return f"Match error at position {pos}"

    return f"Ok - {count}"