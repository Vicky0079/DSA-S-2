def sum_digits(num):
    sum = 0
    while num > 0:
     sum+=num%10
     num/=10
    return sum
print(sum_digits(123))

# time complexity of this program is O(log n)
# becouse here it divide the input  by 10 
# so we have log relationship between time and input size    