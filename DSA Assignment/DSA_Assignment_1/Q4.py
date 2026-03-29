def binary_search(arr, low, high, key):
    if low > high:
        return -1   # Element not found

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)


# ---- Taking input from user ----
arr = list(map(int, input("Enter sorted array elements (space separated): ").split()))
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

# -------------------------------------------------------
# Recurrence Based Complexity Explanation
# Recursive Binary Search
# -------------------------------------------------------
# In recursive binary search, at each step:
# - We divide the array into two halves.
# - We continue searching only in one half.
# - One comparison is performed at each step.
# If the size of the array is n,
# after one recursive call the size becomes n/2.
# Therefore, the recurrence relation is:
# T(n) = T(n/2) + 1
# Explanation:
# T(n/2)  -> time taken to solve smaller subproblem
# +1      -> time for comparison at current step
# Now solving the recurrence:
# After 1 step:
# T(n) = T(n/2) + 1
# After 2 steps:
# T(n) = T(n/4) + 2
# After 3 steps:
# T(n) = T(n/8) + 3
# After k steps:
# T(n) = T(n / 2^k) + k
# Recursion stops when:# n / 2^k = 1
# So,
# n = 2^k
# Taking log on both sides:# k = log2(n)
# Therefore,
# T(n) = O(log n)
# Time Complexity: O(log n)
# Space Complexity: O(log n) (due to recursion stack)