#Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k
def count_pairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1
    return count

nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(count_pairs(nums, k))  

# Output: 4
