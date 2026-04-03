def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Step 1: Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Step 2: Merge
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0  # pointer for left
    j = 0  # pointer for right

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 🔥 Test
arr = [5, 2, 4, 1]
print(merge_sort(arr))