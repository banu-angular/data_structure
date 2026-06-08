
# 📚 Stack Data Structure (Python)

## 🧠 What is a Stack?

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

> 💡 Think of it like a stack of plates — the last plate you put on top is the first one you take off.

----------

## 🎯 Purpose of Stack

-   Manage function calls (call stack)
-   Undo/Redo operations (text editors)
-   Expression evaluation (infix → postfix)
-   Backtracking (DFS, recursion)

----------

## ⚙️ Core Operations

| Operation   | Description                      |
| ----------- | -------------------------------- |
| `push(x)`   | Add element `x` to the top       |
| `pop()`     | Remove top element               |
| `peek()`    | Get top element without removing |
| `isEmpty()` | Check if stack is empty          |


----------

## ⏱️ Time Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |
| Search    | O(n)            |


----------

## 🧩 Mental Model

```
Top
 ↓
| 30 |
| 20 |
| 10 |
```

-   Push → Adds on top
-   Pop → Removes from top

----------

## 🔧 Python Implementation

### ✅ Using List

```
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

# Pop
print(stack.pop())  # 30

# Peek
print(stack[-1])    # 20

# Check if empty
print(len(stack) == 0)
```

----------

### ✅ Using Class (Clean OOP)

```
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"

    def is_empty(self):
        return len(self.items) == 0
```

----------

## 🔄 Step-by-Step Execution

```
stack = []
stack.append(10)  # [10]
stack.append(20)  # [10, 20]
stack.append(30)  # [10, 20, 30]

stack.pop()       # removes 30 → [10, 20]
```

----------

## 🌍 Real-World Examples

### 1. 🔙 Undo Feature

-   Every action pushed into stack
-   Undo → pop last action

### 2. 🌐 Browser History

-   Back button uses stack

### 3. 🧮 Expression Evaluation

-   Used in compilers & calculators

----------

## 🚨 Common Mistakes

-   ❌ Popping from empty stack → Error
-   ❌ Using wrong end (Stack must be LIFO)
-   ❌ Forgetting boundary checks

----------

## 🔥 Important Patterns

-   Reversal problems
-   Balanced parentheses
-   Monotonic stack (Next Greater Element)
-   DFS traversal

----------

## 🧪 Practice Problems

-   Valid Parentheses
-   Next Greater Element
-   Min Stack
-   Reverse a Stack

----------

## 🧾 Summary

-   Stack = LIFO structure
-   Fast operations (O(1))
-   Used in recursion, parsing, undo systems
-   Easy to implement using Python list