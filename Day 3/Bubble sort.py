def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# Test cases
print(bubble_sort([5, 2, 9, 1, 5, 6]))
print(bubble_sort([10, 8, 6, 4, 2]))
print(bubble_sort([1, 2, 3, 4, 5]))
