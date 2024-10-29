def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val
# Test cases
# Input 1
test_case_1 = [5, 7, 3, 4, 9, 12, 6, 2]
min_val_1, max_val_1 = find_min_max(test_case_1)
print("Input 1: Min =", min_val_1, ", Max =", max_val_1)
# Input 2
test_case_2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
min_val_2, max_val_2 = find_min_max(test_case_2)
print("Input 2: Min =", min_val_2, ", Max =", max_val_2)
# Input 3
test_case_3 = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
min_val_3, max_val_3 = find_min_max(test_case_3)
print("Input 3: Min =", min_val_3, ", Max =", max_val_3)
