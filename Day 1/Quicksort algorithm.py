def quicksort(nums):
    if len(nums) <= 1:
        return nums 
    left = []
    right = []
    for num in nums[:-1]:  
        if num < pivot:
            left.append(num)  
        else:
            right.append(num) 
    return quicksort(left) + [pivot] + quicksort(right)
# Example usage:
nums = [3, 4, 6, -9, 10, 8, 9, 30]
sorted_nums = quicksort(nums)
print("Sorted array:", sorted_nums)
