def median_of_medians(arr):
    arr.sort()
    return arr[len(arr) // 2]
def partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return left, right
def select_kth(arr, k):
    if len(arr) == 1:
        return arr[0]    
    pivot = median_of_medians(arr)
    left, right = partition(arr, pivot)
    if k < len(left):
        return select_kth(left, k)
    elif k < len(left) + len(right):
        return pivot
    else:
        return select_kth(right, k - len(left) - len(right))
arr = [12, 3, 5, 7, 19]
k = 2
print(select_kth(arr, k))
