# Recursive Factorial (Naive)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Taking input from user
num = int(input("Enter a number for factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))

# Recursive Factorial (Memoized)

def factorial_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 1

    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]

# Taking input from user
num = int(input("Enter a number for factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial_memo(num))

# Recursive Fibonacci (Naive)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Taking input from user
num = int(input("Enter position for Fibonacci: "))

if num < 0:
    print("Fibonacci is not defined for negative numbers.")
else:
    print("Fibonacci number at position", num, "is", fibonacci(num))

# Recursive Fibonacci (Memoized)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Taking input from user
num = int(input("Enter position for Fibonacci: "))

if num < 0:
    print("Fibonacci is not defined for negative numbers.")
else:
    print("Fibonacci number at position", num, "is", fibonacci_memo(num))

