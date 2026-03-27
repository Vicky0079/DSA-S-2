def power(num):
    if num < 1:
        return 0
    elif num == 1:
        print(1)
        return 1    
    else:
        prev = power(num//2)
        curr = prev*2
        print(curr)
        return curr
n = int(input('enter a number: '))
print(power(n))

# time complexity of this program is
# here we see how many times the function is called that is log(n) times so we have O(log(n)) time complexity
# becouse if we put n=10 then we have 10,5,2,1 so we have 4 function call 
# and if we put n=100 then we have 100,50,25,12,6,3,1 so we have 7 function call 
# and if we put n=1000 then we have 1000,500,250,125,62,31,15,7,3,1 so we have 10 function call 
# so we can say that time complexity of this program is O(log(n))

# input = 10     100     1000
# output = 4       7       10

# input is  multipley and output is add so we can say that time complexity of this program is 
# logarithmic relationship between time and input size


