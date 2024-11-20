from itertools import combinations
def meet_in_the_middle(arr, target):
    half1 = arr[:len(arr)//2]
    half2 = arr[len(arr)//2:]
    def subset_sums(nums):
        sums = []
        for r in range(len(nums)+1):
            sums.extend([sum(comb) for comb in combinations(nums, r)])
        return sums
    sums1 = subset_sums(half1)
    sums2 = subset_sums(half2)
    closest_sum = float('inf')
    for sum1 in sums1:
        for sum2 in sums2:
            total = sum1 + sum2
            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total    
    return closest_sum
arr = [45, 34, 4, 12, 5, 2]
target = 42
result = meet_in_the_middle(arr, target)
print("Closest sum to target:", result)
