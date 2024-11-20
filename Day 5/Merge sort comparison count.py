def merge_sort(arr, counter):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left, counter)
        merge_sort(right, counter)
        i = j = k = 0
        while i < len(left) and j < len(right):
            counter[0] += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        arr[k:] = left[i:] + right[j:]
def count_sort(arr):
    counter = [0]
    merge_sort(arr, counter)
    return arr, counter[0]
# Test cases
test1 = [12, 4, 78, 23, 45, 67, 89, 1]
test2 = [38, 27, 43, 3, 9, 82, 10]
print(count_sort(test1)) 
print(count_sort(test2))  
