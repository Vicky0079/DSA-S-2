l = [1,2,3,4,5]

for i in range(0, len(l)):
    for j in range(i+1,len(l)):
     print('({},{})'.format(l[i],l[j]))

# # time complexity of this program is
# here we have 2 loop they are nested  they are dependent loop
# out loop run n time and inner loop run n-1 time so we have n*(n-1) time complexity
# O(n)*o(n-1)=o(n*(n-1))=o(n^2-n)=o(n^2) 
# we can ignore -n because n^2 is more dominant than n so we have O(n^2) time complexity

A = [1,2,3,4]
B = [2,3,4,5]

for i in A:
   for j in B:
      for k in range(100000):
         print('({},{})'.format(i,j))

# time complexity = O(n)XO(n),O(1)
#                 = O(n^2)

# becouse we have 3 loop but the last loop is not dependent on
# the first two loop so we can ignore it and we have O(n^2) time complexity

# The last loop is constant time complexity because it run 100000 time
# which is constant and does not depend on the size of the input.

