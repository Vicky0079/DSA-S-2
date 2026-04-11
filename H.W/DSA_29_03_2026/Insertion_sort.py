def insertion(arr1):
    n = len(arr1)
    for i in range(1,n):
        key = arr1[i]
        j=i-1
        while j>=0 and key<arr1[j]:
            arr1[j+1] = arr1[j]
            j-=1
        arr1[j+1] = key

arr1 = [40,30,20,10]
insertion(arr1)
print("Sorted array is" ,arr1)

        