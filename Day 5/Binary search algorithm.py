def binary_search(arr, key):
    left, right, comparisons = 0, len(arr) - 1, 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == key:
            return mid + 1, comparisons
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons
# Test case
arr, key = [5, 10, 15, 20, 25, 30, 35, 40, 45], 20
pos, comps = binary_search(arr, key)
print(f"Position: {pos}, Comparisons: {comps}")
