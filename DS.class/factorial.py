def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

num = int(input("Enter your number : "))

if num < 0:
    print("Factorisl is not define for negative number")
else:
    print("Factorial of" ,num ,"is" ,factorial(num))