def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Middle element as pivot
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
arr = [19, 72, 35, 46, 58, 91, 22, 31]
print("Input Array:", arr)
print("Sorted Array:", quick_sort(arr))
