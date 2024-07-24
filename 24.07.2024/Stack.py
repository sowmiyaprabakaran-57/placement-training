class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack Underflow"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is Empty"

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop(), "popped from stack")
print("Top element is", s.peek())
