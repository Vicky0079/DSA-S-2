nums = [2,4,6,7,9,11,18,19]
target = 13

def binarysearch(nums, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarysearch(nums, mid + 1, high, target)
    else:
        return binarysearch(nums, low, mid - 1, target)

result = binarysearch(nums, 0, len(nums)-1, target)

print(result)