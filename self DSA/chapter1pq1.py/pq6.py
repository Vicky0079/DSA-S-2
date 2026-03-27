l = [1,2,3,4,5]
for i in range(0, len(l)//2):
 other = len(l)-1-i
temp = l[i]
l[i] = l[other]
l[other] = temp
print(l)

# time complexity of this program is
# here we have 1 loop which run n/2 time so we have O(n/2) time complexity
# we can ignore 1/2 because it is constant so we have O(n) time complexity