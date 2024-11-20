def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # First element as pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
if __name__ == "__main__":
    arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    print("Input Array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted Array:", sorted_arr)
