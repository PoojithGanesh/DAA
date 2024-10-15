def find_kth_missing(arr, k):
    idx = 0  
    current = 1  
    while k > 0:
        if idx >= len(arr) or arr[idx] != current:
            k -= 1  
            if k == 0:
                return current  
        else:
            idx += 1  
        current += 1  
    return current
# Test cases
print(find_kth_missing([2, 3, 4, 7, 11], 5))  # Expected Output: 9
print(find_kth_missing([1, 2, 3, 4], 2))      # Expected Output: 6
