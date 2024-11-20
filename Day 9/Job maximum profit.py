import bisect
def maxProfit(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    dp = [0] * len(jobs)
    dp[0] = jobs[0][2]
    for i in range(1, len(jobs)):
        current_profit = jobs[i][2]
        last_non_overlap = bisect.bisect_right([job[1] for job in jobs], jobs[i][0]) - 1
        if last_non_overlap != -1:
            current_profit += dp[last_non_overlap]
        dp[i] = max(dp[i - 1], current_profit)
    return dp[-1]
# Test cases
print(maxProfit([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # Output: 120
print(maxProfit([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # Output: 150
