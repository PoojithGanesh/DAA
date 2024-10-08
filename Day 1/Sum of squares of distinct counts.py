'''You are given a 0-indexed integer array nums. The distinct count of a subarray of nums is defined as: Let nums[i..j] be a subarray of nums consisting of all the 
indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j]. Return the sum 
of the squares of distinct counts of all subarrays of nums. A subarray is a contiguous non-empty sequence of elements within an array.'''
def sum_of_squares(nums):
    total_sum = 0
    for i in range(len(nums)):
        distinct_elements = []
        for j in range(i, len(nums)):
            if nums[j] not in distinct_elements:
                distinct_elements.append(nums[j])
            total_sum += len(distinct_elements) ** 2
    return total_sum
nums = [1, 2, 1]
print(sum_of_squares(nums)) 

# Output: 15

'''Explanation:
For nums = [1, 2, 1]:

Subarray [1] has distinct count 1 → 1^2 = 1
Subarray [1, 2] has distinct count 2 → 2^2 = 4
Subarray [1, 2, 1] has distinct count 2 → 2^2 = 4
Subarray [2] has distinct count 1 → 1^2 = 1
Subarray [2, 1] has distinct count 2 → 2^2 = 4
Subarray [1] has distinct count 1 → 1^2 = 1
Sum of squares = 1 + 4 + 4 + 1 + 4 + 1 = 15.'''
