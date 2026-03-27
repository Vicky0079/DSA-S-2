def fibo(n):
     if n == 1 or n == 0:
         return 1
     else:
         return fibo(n-1)+fibo(n-2)
     
# time complexity of this program is
# here we see how many times the function is called  that is 2^n times so we have O(2^n) time complexity
# becouse if we put n=1 then we have 1 function call and if we put n=2 then we have 2 function call
# and if we put n=3 then we have 4 function call and if we put n=4 then we have 8 function call 
# and if we put n=5 then we have 14 function call so we can say that time complexity of this program is O(2^n)
# or less than it
# input = 1   2   3   4    5
# output= 1   2   4   8    14
# becouse we can see almost double function call when we increase n by 1 so we can say that
# time complexity of this program is exponential relationship between time and input size
