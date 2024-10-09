def findPaths(m, n, N, i, j):
    MOD = 1000000007
    dp = [[[0] * n for _ in range(m)] for _ in range(N+1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp[0][i][j] = 1
    result = 0
    for k in range(1, N+1):
        for x in range(m):
            for y in range(n):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        result = (result + dp[k-1][x][y]) % MOD
                    else:
                        dp[k][nx][ny] = (dp[k][nx][ny] + dp[k-1][x][y]) % MOD            
    return result

# Example usage
print(findPaths(2, 2, 2, 0, 0))  # Output: 6
print(findPaths(1, 3, 3, 0, 1))  # Output: 12
