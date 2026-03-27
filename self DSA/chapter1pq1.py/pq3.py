def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i//10
    return result

print(intToStr(123))

# Time complexity of this program is O(log n)
     
# Inp 123     1230    12300    123000
#     10time  10time  10time   10time
# T    3       4       5        6 HOW Many time loop run
#      +1     +1      +1       +1

# if we see here we have 10time input size and we have +1 time so we have log relationship between time and input size
    
