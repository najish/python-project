class Stack:

    def __init__(self, size=10):
        self.items = []
        self.max_size = size

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            raise Exception("Stack overflow")
        
    def pop(self):
        if self.items:
            return self.items.pop()
        else: 
            raise Exception("Stack underflow")
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            raise Exception("Stack is empty")
        
    def is_empty(self):
        return len(self.items) == 0
    
    def current_size(self):
        return len(self.items)
    

def run():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top element:", stack.peek())
    print("Stack size:", stack.current_size())
    print("Popped element:", stack.pop())
    print("Is stack empty?", stack.is_empty())
    # Test overflow
    stack.push(4)
    stack.push(5)
    stack.push(6)  # This should raise "Stack overflow"

if __name__ == "__main__":
    run()
