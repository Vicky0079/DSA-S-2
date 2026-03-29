# 📘 Unit 2 Assignment – Data Structures

## 👤 Student Details
- **Name:** Vicky  
- **Program:** B.Tech CSE (Core)  
- **Section:** A  

---

## 📌 Assignment Overview
This assignment focuses on implementing fundamental data structures and analyzing their performance.

The following topics are covered:
- Dynamic Array (with resizing & amortized analysis)
- Singly Linked List (SLL)
- Doubly Linked List (DLL)
- Stack using SLL
- Queue using SLL
- Parentheses Checker using Stack

---

## 🧩 Implementations

### 🔹 1. Dynamic Array
- Supports:
  - `append()` (with resizing)
  - `pop()`
- Uses doubling strategy for resizing

**Time Complexity:**
- Append → O(1) amortized  
- Pop → O(1)

---

### 🔹 2. Singly Linked List (SLL)
- Operations:
  - Insert at beginning
  - Insert at end
  - Delete
  - Traverse

**Time Complexity:**
- Insert (head) → O(1)  
- Insert (end) → O(n)  
- Traversal → O(n)

---

### 🔹 3. Doubly Linked List (DLL)
- Features:
  - Forward and backward traversal
  - Uses `prev` and `next` pointers

**Time Complexity:**
- Insert/Delete → O(1) (given node)  
- Traversal → O(n)

---

### 🔹 4. Stack using SLL
- Follows **LIFO (Last In First Out)**
- Operations:
  - Push
  - Pop
  - Peek

**Time Complexity:**
- All operations → O(1)

---

### 🔹 5. Queue using SLL
- Follows **FIFO (First In First Out)**
- Operations:
  - Enqueue
  - Dequeue

**Time Complexity:**
- All operations → O(1)

---

### 🔹 6. Parentheses Checker
- Uses stack to validate expressions
- Checks for balanced brackets: `()`, `{}`, `[]`

**Time Complexity:**
- Time → O(n)  
- Space → O(n)

---

## ▶️ How to Run
1. Make sure Python is installed
2. Run the main file:
   ```bash
   python filename.py