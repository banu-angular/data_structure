
# 📚 Queue Data Structure in Python

## 🧠 Introduction

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

> 📌 The first element added is the first one to be removed.

----------

## 🎯 Real-Life Analogy

Think of a queue at a ticket counter:

-   First person in line gets served first
-   New people join at the end

----------

## 🚀 Why Use Queue?

Queues are used in:

-   🖨️ Printer task scheduling
-   🌐 Network request handling
-   🧵 Multithreading & task queues
-   🔍 Breadth First Search (BFS)
-   🎮 Game loops & simulations

----------

## ⚙️ Core Operations

| Operation    | Description               |
| ------------ | ------------------------- |
| `enqueue(x)` | Add element `x` to rear   |
| `dequeue()`  | Remove element from front |
| `front()`    | Get front element         |
| `isEmpty()`  | Check if queue is empty   |


----------

## ⏱️ Time Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Peek      | O(1)            |


----------

## 🧩 Mental Model

```
Front → [10, 20, 30] ← Rear
```

-   Enqueue → Add at rear
-   Dequeue → Remove from front

----------

## 🐍 Python Implementation

### ✅ Using List (Simple but not optimal)

```
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue
print(queue.pop(0))  # 10

# Front
print(queue[0])      # 20

```

> ⚠️ `pop(0)` is O(n), so not efficient for large data

----------

### ✅ Using `collections.deque` (Recommended)

```
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue
print(queue.popleft())  # 10

# Front
print(queue[0])         # 20
```

----------

### ✅ Using Class (OOP Approach)

```
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue Underflow"

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is Empty"

    def is_empty(self):
        return len(self.items) == 0
```

----------

## 🔄 Step-by-Step Execution

```
queue = []

queue.append(10)  # [10]
queue.append(20)  # [10, 20]
queue.append(30)  # [10, 20, 30]

queue.pop(0)      # removes 10 → [20, 30]
```

----------

## 🌍 Real-World Examples

### 🖨️ Printer Queue

Tasks are processed in order

### 🌐 Web Server Requests

Handled in arrival order

### 🔍 BFS Traversal

Queue ensures level-by-level processing

----------

## 🚨 Common Mistakes

-   ❌ Using list for large queues (slow dequeue)
-   ❌ Confusing FIFO with LIFO
-   ❌ Not checking empty queue before dequeue

----------

## 🔥 Important Patterns

-   BFS (Graphs & Trees)
-   Sliding Window
-   Circular Queue
-   Task Scheduling

----------

## 🧪 Practice Problems

-   Implement Queue using Stacks
-   Circular Queue
-   Sliding Window Maximum
-   Rotten Oranges (BFS)

----------

## 🧾 Summary

-   Queue follows **FIFO**
-   Best implemented using **deque**
-   Used in scheduling, buffering, BFS
-   Essential for system design & real-time processing