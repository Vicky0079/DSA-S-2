# Sorting tecinqe :-
# 1)Compersion
# 2)Loop 
# 3)Swaping
# 4)Time complexity ,space complexity(in place and out place)
# 5)Satble 
# 6)Unstable

# ---------------------------------------------------------------------
# best case (array already sorted)time comlexity is 
# n-1 anything minas in infinty is infinty so time comlexity = O(n)

# def bubble(arr1):
#     n = len(arr1)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr1[j]>arr1[j+1]:
#                 arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
#                 swapped = True
#             if not swapped:
#                 break
# arr1=[10,20,30,40]
# bubble(arr1)
# print("sorted array is:",arr1)

# ----------------------------------------------------------------------
# worst case (array in decinding order)time complexity is

def bubble(arr1):
    n = len(arr1)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                swapped = True
        if not swapped:
                break
arr1=[40,30,20,10]
bubble(arr1)
print("sorted array is:",arr1)
