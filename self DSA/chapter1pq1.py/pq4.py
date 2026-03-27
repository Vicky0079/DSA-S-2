A=[1,2,3,4]
B=[2,3,4,5,6]

for i in A:
    for j in B:
        if i<j:
            print('({},{})'.format(i,j))
# time complexity of this program is
# here we have 2 loop they are nested  they are dependent loop
# O(n)*o(m)=o(n*m) is more corect than O(n^2) because we have 2 different input size n and m
# but O(n^2) is also correct 