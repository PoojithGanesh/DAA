def can_assign(jobs, k, max_time):
    workers = [0] * k
    def backtrack(index):
        if index == len(jobs):
            return True
        for i in range(k):
            if workers[i] + jobs[index] <= max_time:
                workers[i] += jobs[index]
                if backtrack(index + 1):
                    return True
                workers[i] -= jobs[index]
            if workers[i] == 0:  # No jobs assigned to this worker
                break
        return False
    return backtrack(0)
def minimum_maximum_working_time(jobs, k):
    low, high = max(jobs), sum(jobs)
    while low < high:
        mid = (low + high) // 2
        if can_assign(jobs, k, mid):
            high = mid
        else:
            low = mid + 1
    return low
# Example usage
print(minimum_maximum_working_time([3, 2, 3], 3))  # Output: 3
print(minimum_maximum_working_time([1, 2, 4, 7, 8], 2))  # Output: 11
