def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1   
        arr[j + 1] = key  
    return arr
# Test cases
print(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])) # Array with duplicates
print(insertion_sort([5, 5, 5, 5, 5]))                # All identical elements
print(insertion_sort([2, 3, 1, 3, 2, 1, 1, 3]))       # Mixed duplicates
