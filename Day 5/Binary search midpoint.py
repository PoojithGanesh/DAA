def binary_search(arr, key):
    left, right, comparisons = 0, len(arr) - 1, 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        print(f"Left: {left}, Right: {right}, Mid: {mid}, Mid Value: {arr[mid]}")
        if arr[mid] == key:
            return mid + 1, comparisons
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons
# Test case
arr = [3, 9, 14, 19, 25, 31, 42, 47, 53]
key = 31
pos, comps = binary_search(arr, key)
print(f"Position: {pos}, Comparisons: {comps}")
