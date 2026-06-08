class Stack:
    def __init__(self):
        self.top = -1
        self.stack = [] 

    def push(self, item):
        self.top = self.top + 1
        self.stack.append(item) 
        
    def pop(self):
        if(len(self.stack) == 0):
            print("Stack is empty")
            return            
        print("Popping an element:", self.stack[self.top])
        self.stack.pop()
        self.top = self.top - 1
        
    def peek(self):
        if(len(self.stack) == 0): 
            print("Stack is empty")
            return
            
        print("Peeking an element:", self.stack[self.top])

if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(23)
    stack1.push(24)
    stack1.push(25)
    stack1.pop()
    stack1.peek()