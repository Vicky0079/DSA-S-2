def mod(a,b):

    if b<=0:
        return -1
    div = a//b
    return a-div*b

mod(5,3)

# time complexity of this program is  constant
# becouse it has only arithmetic operation and 
# it does not depend on the input size so we have O(1) time complexity