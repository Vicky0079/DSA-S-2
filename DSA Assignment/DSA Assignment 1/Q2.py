# Time and Space Complexity of Recursive Factorial and Recursive Fibonacci (Naive)

# 1️⃣ Recursive Factorial (Naive)
# Factorial is defined as:
# n! = n × (n-1)!
# Time Complexity:
# Each function call makes only one recursive call.
# Total number of calls = n
# Recurrence relation:
# T(n) = T(n-1) + 1
# Therefore,
# Time Complexity = O(n)
# Space Complexity:
# Each recursive call is stored in the call stack.
# Maximum stack depth = n
# Therefore,
# Space Complexity = O(n)

# 2️⃣ Recursive Fibonacci (Naive)
# Fibonacci is defined as:
# F(n) = F(n-1) + F(n-2)
# Time Complexity:
# Each function call makes two recursive calls.
# Many values are calculated repeatedly.
# Recurrence relation:
# T(n) = T(n-1) + T(n-2)
# This grows exponentially.
# Therefore,
# Time Complexity = O(2ⁿ)
# Why Naive Fibonacci is Inefficient?
# Because of overlapping subproblems.
# The same Fibonacci values are calculated multiple times, which causes:
# Large number of recursive calls
# Exponential growth
# Very slow performance for large n
# Space Complexity:
# Maximum recursion depth = n
# Therefore,
# Space Complexity = O(n)
# ----------------------------------------------------------
# Recursive Factorial → Time: O(n), Space: O(n)
# Recursive Fibonacci (Naive) → Time: O(2ⁿ), Space: O(n)