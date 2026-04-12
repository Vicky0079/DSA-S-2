nums = [3,1,2,4,1,5,2,6,4]

def merge_sort(arr):
    print("\n➡️ merge_sort CALLED with:", arr)

    if len(arr)<=1:
        print("⬅️ RETURN (base case):", arr)
        return arr

    mid = len(arr)//2
    print("🔹 mid index:", mid)

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    print("   Left part:", left_arr)
    print("   Right part:", right_arr)

    left = merge_sort(left_arr)
    print("⬆️ Back from LEFT call with:", left)

    right = merge_sort(right_arr)
    print("⬆️ Back from RIGHT call with:", right)

    print("🔸 Now calling merge_array with:", left, right)

    result = merge_array(left,right)

    print("⬅️ RETURN (merged result):", result)
    return result


def merge_array(left,right):
    print("\n🟡 merge_array CALLED with:", left, right)

    result = []
    i,j = 0,0
    n,m = len(left),len(right)

    while i<n and j<m:
        print("   Comparing:", left[i], "and", right[j])

        if left[i] <= right[j]:
           print("   👉 Taking from LEFT:", left[i])
           result.append(left[i])
           i+=1
        else:
            print("   👉 Taking from RIGHT:", right[j])
            result.append(right[j])
            j+=1

        if i<n:
            print("   (LEFT still has elements)")
            while i<n :
                print("   ➕ Adding remaining LEFT:", left[i])
                result.append(left[i])
                i+=1

        if j<m:
            print("   (RIGHT still has elements)")
            while j<m :
                print("   ➕ Adding remaining RIGHT:", right[j])
                result.append(right[j])
                j+=1

    print("🟢 merge_array RETURN:", result)
    return result


print("\n===== START =====")
print(merge_sort(nums))
print("===== END =====")