def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)
# Test cases
print(merge_sort([31, 23, 35, 27, 11, 21, 15, 28]))  # Output: [11, 15, 21, 23, 27, 28, 31, 35]
print(merge_sort([22, 34, 25, 36, 43, 67, 52, 13, 65, 17]))  # Output: [13, 17, 22, 25, 34, 36, 43, 52, 65, 67]
