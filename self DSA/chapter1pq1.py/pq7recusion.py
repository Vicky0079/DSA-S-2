def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# time complexity of this program is
# here we see how many times the function is called  that is 5 times so we have O(n) time complexity
# becouse if we put n=5 then we have 5*4*3*2*1 so we have 5 function call and if we put n=6 then 
# we have 6*5*4*3*2*1 so we have 6 function call so we can say that time complexity of this program is O(n)
# that show that time complexity of this program is linear relationship between time and input size